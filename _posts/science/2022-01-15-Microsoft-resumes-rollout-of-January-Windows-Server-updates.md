---
layout: post
title: "Microsoft resumes rollout of January Windows Server updates"
author: jane 
date: 15-01-2022 14:47:47 +05:30 
categories: [ TECHNOLOGY ] 
image: assets/images/15-01-2022/windows-server-black-hole.jpg
---
The January 2022 Windows Server cumulative updates are once again available via Windows Update after being pulled yesterday without an official reason from Microsoft.

On Tuesday, Microsoft released the January 2022 Patch Tuesday cumulative updates, with the KB5009624 update for Windows Server 2012 R2, KB5009557 for Windows Server 2019, and KB5009555 for Windows Server 2022.

After Windows admins installed the updates, some found that it caused their Windows Servers to go into boot loops, ReFS volumes to become inaccessible, and Hyper-V not to start.

After the numerous problems, Windows admins told BleepingComputer, and our own tests showed, Windows Update no longer offered the new Windows Server updates. However, they were still available via WSUS and through the Microsoft Catalog.

Windows Server 2019 not offered the January 2022 update

When we asked Microsoft why they pulled the updates from Windows Update, we were only told that "Microsoft is aware and investigating the issue."

Starting today, the Windows Server updates are available via Windows Update once again without any reason from Microsoft why they initially pulled them.

Windows Server updates back in Windows Update

Microsoft has also officially confirmed the boot loop and Hyper-V problems as "known issues" in the Windows message center.

"After installing KB5009557 on domain controllers (DCs), affected versions of Windows Servers might restart unexpectedly," explains a new known issue regarding the domain controller reboots.

"Note: On Windows Server 2016 and later, you are more likely to be affected when DCs are using Shadow Principals in Enhanced Security Admin Environment (ESAE) or environments with Privileged Identity Management (PIM)."

For Windows Server 2012 R2, Microsoft also created a new known issue for the Hyper-V problems, stating it is affecting devices using UEFI.

Microsoft says they are investigating both issues and will release a fix in a future update.