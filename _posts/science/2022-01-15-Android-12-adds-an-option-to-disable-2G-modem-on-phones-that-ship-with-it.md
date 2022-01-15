---
layout: post
title: "Android 12 adds an option to disable 2G modem on phones that ship with it"
author: jane 
date: 15-01-2022 14:47:42 +05:30 
categories: [ TECHNOLOGY ] 
image: assets/images/15-01-2022/Android-12-no-2G.jpg
---
Android 12 adds an option to disable 2G modem on phones that ship with it

We’ve hearing about Android 13 for a bit now, including our first look at it, but that doesn’t mean we stop paying attention to Android 12 already. As the update rolls out to more devices, and more new phones ship with this latest version of Android, we discover new changes that have flown under the radar. One such change has now been spotted, as Android 12 comes with an option to disable 2G modems on phones that ship with it.

As The Electronic Frontier Foundation (EFF) reports (via Mishaal Rahman), Android 12 has quietly added an option to disable 2G at the modem level.

This may sound like a very small change, but it does have some serious repercussions and you should probably consider switching it off on your device. As the original report notes, 2G is the second generation of mobile communication, created back in 1991, and its age shows with the many vulnerabilities that have since been found. 2G uses weak encryption between the tower and device, and this can be cracked in real-time by an attacker to intercept calls and text messages. There is no authentication of the tower to the phone either, opening up the ability to impersonate a real 2G tower. Cell-site simulators, aka “stingrays” exploit these methods to intercept communications. They can downgrade your connection from 4G to 2G, and then apply the above attacks. So if you value your privacy and other rights, it becomes important for you to steer clear of 2G if you can.

There are some limitations here that you should be aware of, though. As Mishaal points out, this feature requires an update to the Radio HAL, which many older devices upgrading from Android 11 to Android 12 will be skipping out on because of GRF (Google Requirements Freeze). Devices shipping with Android 12 will be in a position to present this change to users. As EFF notes, on newer Pixels and Samsung devices (some even on Android 11 as Samsung has an implementation for this Android version also), you can disable 2G by toggling the option at Settings > Network & Internet > SIMs > Allow 2G. But from what we know, doing so will present a rather annoying and persistent notification on Samsung devices.

Further, disabling 2G also comes at the cost of disabling access to emergency services in regions where only 2G service is available, which is a rather heavy cost if you ask me. While most carriers have adopted 4G for a big chunk of their infrastructure, there are pockets that still remain serviceable only with 2G — so please be very careful and assess the impact this can have on you and others around you.

If you don’t have the option on your device, there are some options you can explore. Custom ROMs like Graphene OS, a security-focused distribution of Android, present users with an LTE-only mode as a way to reduce the attack surface on the device.

You can also use Android Dialer Codes, namely *#*#4636#*#*, navigate to Phone Information 1, and set your preferred network type as LTE (4G) or NR/LTE (5G/4G) only — however keep in mind that the setting will reset on reboot. Note that these LTE-only options also switch off 3G, but you can retain 3G use in Dialer Code by instead adopting one of the 3G options relevant to your network region. Further, keep in mind that if your network operator does not support VoLTE, you will lose calling and texting services if you adopt LTE-only. As mentioned, lots of limitations, so make the decision that makes the best sense for you.

2g icon by Icons8