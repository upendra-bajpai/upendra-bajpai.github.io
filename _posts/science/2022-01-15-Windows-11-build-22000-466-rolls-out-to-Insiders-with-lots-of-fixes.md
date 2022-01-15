---
layout: post
title: "Windows 11 build 22000.466 rolls out to Insiders with lots of fixes"
author: jane 
date: 15-01-2022 14:47:01 +05:30 
categories: [ TECHNOLOGY ] 
image: assets/images/15-01-2022/Windows-11-option-2.jpg
---
Windows 11 build 22000.466 rolls out to Insiders with lots of fixes

This month’s Patch Tuesday was seemingly light on fixes for Windows users, but Windows Insiders in the Beta and Release Preview channels are getting some extra improvements today. Microsoft is rolling out Windows 11 build 22000.466, and as usual for builds in the Beta channel, it’s all about fixing and improving various issues with the experience.

While it’s mostly about fixes, there is one addition tucked away in this build’s changelog. You’ll now see a Your Microsoft Account page in the Accounts section of the Settings app. This is being added in Windows 11 Home and Pro editions.

The list of changes includes a wide range of fixes, including one for an issue that might have caused ARM64-based devices such as the Surface Pro X to become unresponsive when hibernating or waking from hibernation. Installing apps on ARM PCs should also be more reliable now. You can find the full list below:

What's new in Windows 11 build 22000.466 We improved the reliability of application installations on ARM64 devices.

We updated daylight savings time to start in February 2022 instead of March 2022 in Jordan.

We fixed an issue that causes ARM64 devices to stop responding when they hibernate or resume from hibernation.

We fixed an issue that might prevent some image editing programs from rendering colors correctly on certain high dynamic range (HDR) displays. This frequently affects white colors that might display in bright yellow or other colors.

We fixed an issue that affects predictive pre-rendering in Microsoft Edge Internet Explorer mode.

We fixed an issue that sometime prevents you from entering strings in the Input Method Editor (IME).

We fixed an issue that causes the audio service to stop responding on some devices that support hardware-accelerated Bluetooth audio.

We fixed an issue in which the text that informs a customer about the Windows update progress is incorrect for Japanese.

We fixed an issue that affects icons for apps when the apps are not running. On the taskbar, these icons might display as active as if the apps are running.

We fixed an issue that might cause VPN profiles to disappear. This issue occurs when you use Microsoft Intune or a third-party mobile device management (MDM) tool to deploy VPN profiles on Windows 11 (original release).

We fixed an issue that affects applications that are written to only integrate with Azure Active Directory (AAD). These applications will not work on machines that are joined to Active Directory Federation Services (ADFS).

We fixed an issue that might cause the Get-TPM PowerShell command to fail when it attempts to report Trusted Platform Module (TPM) information. The command fails with the error, “0x80090011 Microsoft.Tpm.Commands.TpmWmiException,Microsoft.Tpm.Commands.GetTpmCommand”.

PowerShell command to fail when it attempts to report Trusted Platform Module (TPM) information. The command fails with the error, “0x80090011 Microsoft.Tpm.Commands.TpmWmiException,Microsoft.Tpm.Commands.GetTpmCommand”. We fixed an issue that causes a remote desktop protocol (RDP) session to disconnect or the screen to be blank for Server Core. This issue occurs when you install the AppCompat feature.

We fixed an issue that affects windows.system.profile.retailinfo.dll .

. We fixed some issues that affect File Explorer’s performance when you browse for files and select files.

We added a new Your Microsoft Account page to the Accounts category in Windows Settings for Home and Professional editions.

page to the Accounts category in Windows Settings for Home and Professional editions. We fixed an issue that incorrectly shows the volume icon in the taskbar as muted.

We fixed a reliability issue that causes File Explorer and desktop context menus to stop working.

We fixed an issue that fails to pass the Shift KeyUp event to an application when you use the Korean IME.

We added the HelpWith feature, which uses Microsoft Bing technologies to suggest Help topics that are relevant for each Settings page.

We fixed an issue that prevents the touch keyboard from appearing on the lock screen when a device has a Microsoft account (MSA).

We fixed an issue that affects the loading of badging information on the taskbar, which sometimes causes a device to stop working.

We fixed an issue that prevents some options from appearing on the Win + X menu.

We fixed an issue that causes a device to stop working when it’s connected to multiple displays.

We fixed an issue that affects the auto-hide feature of the taskbar. The taskbar might not reliably appear when you hover over the primary or secondary display.

We fixed an issue that sometimes prevents you from using the Chinese Simplified IME.

We fixed an issue that might prevent icons from appearing on the taskbar of a secondary display.

We fixed an issue that fails to install certain printer companion applications when the printer device driver is installing.

We fixed an issue that displays outdated battery percentages for connected Bluetooth devices on the Bluetooth and other devices page in Settings.

page in Settings. We fixed an issue that prevents IP cameras from connecting and streaming to certain DirectShow (DShow) applications.

We improved the auto brightness algorithm to provide a better response under low light conditions on all the supported systems.

We fixed an issue that causes lsass.exe to stop working and the device restarts. This issue occurs when you query Windows NT Directory Services (NTDS) counters after the NTDS service has stopped.

to stop working and the device restarts. This issue occurs when you query Windows NT Directory Services (NTDS) counters after the NTDS service has stopped. We fixed an issue that causes a deadlock in the WebDav redirector. This issue occurs when you attempt to read a file from the local TfsStore, which causes the system to stop responding.

We fixed a performance regression issue that occurs when you enable the update sequence number (USN) journal.

We fixed an issue that fails to apply the Group Policy Object (GPO) “Do not allow compression on all NTFS Volume” in some cases.

We fixed an issue that prevents Robocopy from retrying the file copy process.

We fixed an issue that causes Windows to stop working and generates the error, “IRQL_NOT_LESS_OR_EQUAL”.

We fixed a memory leak that occurs when you call WinVerifyTrust(). This issue occurs if verification fails for the first signature of a file that has multiple signatures.

As per usual, these fixes should roll out to general users soon. First, there will be a set of optional cumulative updates in the second half of January, when this exact update should be made available to the general public. Then, Microsoft will bundle these fixes into February’s Patch Tuesday update, which is mandatory and should include even more improvements.

Speaking of Patch Tuesday, the latest updates for Windows 11 and 10 seem to be causing some issues for VPN users. If you rely on VPN connections, you might want to wait before installing this month’s updates.