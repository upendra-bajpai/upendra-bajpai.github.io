---
layout: post
title: "Hands on with Windows 10 s new Start Menu"
author: jane 
date: 15-09-2020 12:50:26 
categories: [ TECHNOLOGY ] 
image: assets/images/15-09-2020/Start-Menu.jpg
---
During a Windows Insider webcast, Microsoft teased its vision for a new Windows 10 Start Menu that features partially transparent theme-aware tiles to showcase the new Fluent-based colorful icons.

Microsoft said it will bring the new Start Menu to your devices with Windows 10 version 20H2, which is expected to arrive in October or November.

Start Menu is not getting a dramatic overhaul, but it's getting some subtle changes in the next version.

Currently, we have Start Menu tiles with a colored background, as shown in the screenshot below.

With Windows 10 version 20H2, Microsoft says it will remove the system accent color behind tiles, which will make your live tiles translucent with blur effects, and tiles will finally match with light or dark mode.

According to Microsoft, this will "visually unify the start menu from somewhat chaotic color to something that is more uniform."

As you can see in the above GIF, the next update will fresh up the Start Menu to remove the solid color backplates behind the logos in the apps list and create a beautiful uniform design for your apps, especially Fluent Design-based Office and Microsoft Edge.

It's a minor design refresh, but it looks better and more unified, thanks to the emphasis on the new icon designs.

Unlock Windows 10's new Start Menu now

Starting with Build 19041.423 or newer, you can now unlock the 20H2 features in Windows 10 version 2004 by tweaking your Registry.

The Registry hack highlighted below will allow you to unlock the new Start menu, updated Alt-Tab, and other improvements without upgrading to Windows 10 20H2.

It's important to understand that the Registry Editor is a powerful tool, and it is recommended that you first create a backup of the registry before making any changes.

To unlock 20H2 features, follow these steps:

Open Notepad. Enter the following Registry code: Windows Registry Editor Version 5.00 [HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\FeatureManagement\Overrides\0\2093230218]

"EnabledState"=dword:00000002

"EnabledStateOptions"=dword:00000000 Save it as 20H2.reg Close Notepad. Run .reg file. Restart Windows and you'll have the new Start menu.

If you want to go back to the old layout, simply delete the Registry entries or restore your Registry from backup.