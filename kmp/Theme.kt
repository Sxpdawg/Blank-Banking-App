package com.blank.banking.ui.theme

import androidx.compose.material3.darkColorScheme
import androidx.compose.material3.MaterialTheme
import androidx.compose.runtime.Composable
import androidx.compose.ui.graphics.Color

val AurelianBackground = Color(0xFF000000)
val AurelianSurface = Color(0xFF121212)
val AurelianSurfaceContainerHigh = Color(0xFF2A2A2A)
val AurelianPrimary = Color(0xFFD4AF37)
val AurelianPrimaryVariant = Color(0xFFF2CA50)
val AurelianTextMain = Color(0xFFE5E2E1)
val AurelianTextMuted = Color(0xFFC6C6C6)
val AurelianChromeBorder = Color(0x26FFFFFF) // 15% white

val AurelianSuccess = Color(0xFF34D399)
val AurelianDanger = Color(0xFFF87171)

private val AurelianDarkColorScheme = darkColorScheme(
    background = AurelianBackground,
    surface = AurelianSurface,
    primary = AurelianPrimary,
    onPrimary = Color.Black,
    onBackground = AurelianTextMain,
    onSurface = AurelianTextMain,
    outline = AurelianChromeBorder,
    error = AurelianDanger,
    surfaceVariant = AurelianSurfaceContainerHigh
)

@Composable
fun AurelianTheme(content: @Composable () -> Unit) {
    MaterialTheme(
        colorScheme = AurelianDarkColorScheme,
        // Typography would be configured here using the Inter font family
        content = content
    )
}
