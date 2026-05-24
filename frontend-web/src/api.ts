export const api = {
  getBalance: async () => {
    try {
      // Connects to your FastAPI backend
      const res = await fetch('/api/balance');
      if (res.ok) return await res.json();
    } catch (e) {
      console.warn("Backend not reachable, using placeholder data");
    }
    // Fallback data so the UI looks good while developing
    return { balance: 142500.00 }; 
  },
  
  getTransactions: async () => {
    try {
      const res = await fetch('/api/history');
      if (res.ok) return await res.json();
    } catch (e) {
      console.warn("Backend not reachable, using placeholder data");
    }
    return [
      { id: 1, date: '2026-05-24', description: 'Inbound Wire - APEX CLEARING', amount: 25000.00, type: 'credit' },
      { id: 2, date: '2026-05-22', description: 'AWS Cloud Services', amount: -450.25, type: 'debit' },
      { id: 3, date: '2026-05-21', description: 'Equinox Membership', amount: -300.00, type: 'debit' },
      { id: 4, date: '2026-05-18', description: 'Dividend - VOO', amount: 1250.50, type: 'credit' },
    ];
  },

  transferFunds: async (data: { recipient: string; amount: number }) => {
    const res = await fetch('/api/transfer', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(data)
    });
    if (!res.ok) throw new Error('Transfer failed');
    return await res.json();
  }
};