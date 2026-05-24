import React, { useState, useEffect } from 'react';
import './App.css';
import { api } from './api';

export default function App() {
  const [activeTab, setActiveTab] = useState<'overview' | 'history' | 'transfer'>('overview');
  const [balance, setBalance] = useState<number | null>(null);

  useEffect(() => {
    api.getBalance().then(data => setBalance(data.balance));
  }, []);

  return (
    <div className="app-container">
      {/* Sidebar */}
      <aside className="sidebar">
        <div className="brand">AURELIAN.</div>
        <nav className="nav-links">
          <button 
            className={`nav-btn ${activeTab === 'overview' ? 'active' : ''}`}
            onClick={() => setActiveTab('overview')}
          >
            Overview
          </button>
          <button 
            className={`nav-btn ${activeTab === 'history' ? 'active' : ''}`}
            onClick={() => setActiveTab('history')}
          >
            History
          </button>
          <button 
            className={`nav-btn ${activeTab === 'transfer' ? 'active' : ''}`}
            onClick={() => setActiveTab('transfer')}
          >
            Transfer Funds
          </button>
        </nav>
      </aside>

      {/* Main Content Area */}
      <main className="main-content">
        {activeTab === 'overview' && <Overview balance={balance} />}
        {activeTab === 'history' && <History />}
        {activeTab === 'transfer' && <Transfer setBalance={setBalance} />}
      </main>
    </div>
  );
}

// --- Screens ---

function Overview({ balance }: { balance: number | null }) {
  return (
    <div>
      <h2 style={{ marginBottom: '32px' }}>Dashboard</h2>
      <div className="card">
        <div className="label">Total Liquid Balance</div>
        <div className="balance-display">
          ${balance !== null ? balance.toLocaleString('en-US', { minimumFractionDigits: 2 }) : '---'}
        </div>
        <div style={{ color: 'var(--success)', fontSize: '14px', fontWeight: 500 }}>
          +2.4% Past 30 Days
        </div>
      </div>
    </div>
  );
}

function History() {
  const [transactions, setTransactions] = useState<any[]>([]);

  useEffect(() => {
    api.getTransactions().then(data => setTransactions(data));
  }, []);

  return (
    <div>
      <h2 style={{ marginBottom: '32px' }}>Transaction History</h2>
      <div className="card">
        <table className="data-table">
          <thead>
            <tr>
              <th className="label">Date</th>
              <th className="label">Description</th>
              <th className="label" style={{ textAlign: 'right' }}>Amount</th>
            </tr>
          </thead>
          <tbody>
            {transactions.map(t => (
              <tr key={t.id}>
                <td style={{ color: 'var(--text-muted)' }}>{t.date}</td>
                <td>{t.description}</td>
                <td style={{ textAlign: 'right' }} className={t.type === 'credit' ? 'credit' : 'debit'}>
                  {t.type === 'credit' ? '+' : '-'}${Math.abs(t.amount).toLocaleString('en-US', { minimumFractionDigits: 2 })}
                </td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </div>
  );
}

function Transfer({ setBalance }: { setBalance: (val: number) => void }) {
  const [recipient, setRecipient] = useState('');
  const [amount, setAmount] = useState('');
  const [status, setStatus] = useState<'idle' | 'loading' | 'success' | 'error'>('idle');

  const handleTransfer = async (e: React.FormEvent) => {
    e.preventDefault();
    setStatus('loading');
    try {
      await api.transferFunds({ recipient, amount: parseFloat(amount) });
      setStatus('success');
      // In a real app, you might fetch the new balance here
      setRecipient('');
      setAmount('');
    } catch (err) {
      setStatus('error');
    }
  };

  return (
    <div>
      <h2 style={{ marginBottom: '32px' }}>Transfer Funds</h2>
      <div className="card" style={{ maxWidth: '480px' }}>
        <form onSubmit={handleTransfer}>
          <div className="form-group">
            <label className="label">Recipient Account ID</label>
            <input 
              type="text" 
              className="input-field" 
              value={recipient}
              onChange={e => setRecipient(e.target.value)}
              placeholder="e.g. ACCT-8492"
              required 
            />
          </div>
          <div className="form-group">
            <label className="label">Amount (USD)</label>
            <input 
              type="number" 
              className="input-field"
              value={amount}
              onChange={e => setAmount(e.target.value)}
              placeholder="0.00"
              min="0.01"
              step="0.01"
              required 
            />
          </div>
          <button type="submit" className="btn-primary" disabled={status === 'loading'}>
            {status === 'loading' ? 'Processing...' : 'Submit Transfer'}
          </button>
          
          {status === 'success' && (
            <div style={{ marginTop: '16px', color: 'var(--success)', textAlign: 'center' }}>
              Transfer completed successfully.
            </div>
          )}
          {status === 'error' && (
            <div style={{ marginTop: '16px', color: 'var(--danger)', textAlign: 'center' }}>
              Transfer failed. Please check balance and try again.
            </div>
          )}
        </form>
      </div>
    </div>
  );
}