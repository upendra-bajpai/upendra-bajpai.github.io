---
layout: post
title: "OpenGApps releases Google app packages for Android 11 custom ROMs"
author: jane 
date: 18-07-2021 17:01:46 +05:30 
categories: [ TECHNOLOGY ] 
image: assets/images/18-07-2021/OpenGApps-Banner.jpg
---
OpenGApps releases its first Google app packages for Android 11 custom ROMs

Not many people are willing to use an Android phone without access to the Google Play Store and other Google apps, which is why most Android phones come with Google apps preinstalled. Because Google apps are proprietary, though, many custom ROM developers don’t bundle them with their builds, so they instead tell users to flash community-made Google app bundles commonly referred to as “GApps” packages. One of the most popular GApps packages on XDA is called OpenGApps, and the team behind the project now offers Google app packages compatible with Android 11 custom ROMs.

Android 11-compatible Google app packages are now available from the opengapps.org website. Currently, only “nano” and “pico” variants are available for all four supported architectures (ARM, ARM64, x86, and x86_64). These packages are the smallest in size because they only contain the bare minimum required to get the Google Play Store, Google Play Services, and other key Google services up and running. According to team member nezorflame, the OpenGApps team is still testing the bigger variants which contain more Google apps, though you can always download most Google apps from the Play Store. Android Auto, however, is required to be preinstalled, which is why recent “pico” builds were updated to include its stub package which the Play Store build updates on top of.

The OpenGApps team released Android 10-compatible Google app packages back in January of 2020, four months after the stable release of Android 10. The Android 11-compatible Google app packages come 10 months after the stable release of Android 11 — a much longer wait than before — but keep in mind that the maintainers of the project are all volunteers doing this in their free time, so we have to cut them some slack because they owe us nothing.

Although OpenGApps is the most popular and well-known unofficial GApps package, there are other popular Google app packages that custom ROM developers have pointed users to while updated OpenGApps packages were unavailable. LineageOS, for instance, recommends MindTheGapps for LineageOS 18.1 installs, though they’re moving to now list OpenGApps in their wiki as well.

As for why one may want to use OpenGApps, the developers do a great job at supporting multiple architectures, keeping their Google app packages up-to-date, compressing their files, and building their installer script with intelligent checks to ensure compatibility, automate backups, and allow for customization. Getting Google apps onto an AOSP ROM is not as simple as copying the apps onto the system partition — the installer script has to also set permissions, add overlays, and do other things to make sure the apps behave properly.