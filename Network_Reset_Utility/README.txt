NETWORK RESET UTILITY
Developed by Harper_IDS for IgromanDS Gaming Community

============================================================
AUTHORSHIP: Harper_IDS - All rights reserved for IgromanDS community
============================================================

DESCRIPTION:
This utility is designed to fix network issues caused by VPNs, DNS changes, 
and various network tools (zapret-discord-youtube, nekobox, nekoray, adguard, etc.)
that disrupt Windows 11 network settings.

FEATURES:
- Light Reset: Clear DNS cache only (no restart needed)
- Medium Reset: Clear DNS, ARP, NetBIOS cache and reset Winsock (no restart needed)
- Heavy Reset: Reset TCP/IP stack and network adapters (no restart needed)
- Complete Reset: Full network reset (restart recommended)
- All operations include detailed explanations of what they do, risks, and benefits

USAGE:
1. Run as Administrator (required for all network reset functions)
2. Choose the appropriate reset level based on your issue severity
3. Follow the on-screen instructions

RESET LEVELS:
[1] LIGHT - Clear DNS cache only (Recommended for minor issues)
    - No network interruption
    - Quick and safe
    - Fixes temporary DNS problems

[2] MEDIUM - Clear DNS, ARP, NetBIOS cache and reset Winsock (Recommended for moderate issues)
    - May require reconnecting to WiFi
    - Fixes most cache-related network problems
    - Resets Windows socket layer

[3] HEAVY - Reset TCP/IP stack and network adapters (For persistent issues)
    - Requires network reconnection
    - Fixes deep network stack problems
    - Resets TCP/IP to default state

[4] COMPLETE - Full network reset (For severe issues, restart recommended)
    - Removes all network profiles and configurations
    - Like starting fresh, but requires reconfiguration
    - Total network stack reset

TROUBLESHOOTING:
- Always run as Administrator
- If network issues persist after complete reset, consider updating network drivers
- After heavy or complete reset, you may need to reconfigure WiFi networks and VPN settings

DISCLAIMER:
This tool is provided as-is. Use at your own risk. Always backup important network configurations before using heavy or complete reset options.