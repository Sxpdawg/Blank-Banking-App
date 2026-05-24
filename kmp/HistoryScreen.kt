package com.blank.banking.ui.screens

import androidx.compose.foundation.background
import androidx.compose.foundation.layout.*
import androidx.compose.foundation.lazy.LazyColumn
import androidx.compose.material3.*
import androidx.compose.runtime.Composable
import androidx.compose.ui.Modifier
import androidx.compose.ui.text.font.FontWeight
import androidx.compose.ui.unit.dp
import androidx.compose.ui.unit.sp
import com.blank.banking.ui.theme.AurelianTextMuted

@Composable
fun HistoryScreen() {
    LazyColumn(
        modifier = Modifier
            .fillMaxSize()
            .background(MaterialTheme.colorScheme.background)
            .padding(16.dp)
    ) {
        item {
            Text(
                text = "TRANSACTION HISTORY",
                color = MaterialTheme.colorScheme.primary,
                fontSize = 24.sp,
                fontWeight = FontWeight.Bold,
                modifier = Modifier.padding(vertical = 24.dp)
            )
        }

        val mockData = listOf(
            Triple("Woolworths Food", "-R1,299.00", "Yesterday"),
            Triple("Salary Deposit", "+R38,500.00", "25 Oct 2023"),
            Triple("Eskom Holdings", "-R2,184.20", "24 Oct 2023"),
            Triple("AWS Cloud Services", "-R450.25", "22 Oct 2023"),
            Triple("Inbound Wire - APEX", "+R25,000.00", "20 Oct 2023")
        )

        items(mockData.size) { index ->
            val transaction = mockData[index]
            val isCredit = transaction.second.startsWith("+")
            
            TransactionItemRow(
                title = transaction.first,
                date = transaction.third,
                amount = transaction.second,
                isCredit = isCredit
            )
            
            if (index < mockData.size - 1) {
                Divider(color = MaterialTheme.colorScheme.outline, thickness = 1.dp)
            }
        }
    }
}
