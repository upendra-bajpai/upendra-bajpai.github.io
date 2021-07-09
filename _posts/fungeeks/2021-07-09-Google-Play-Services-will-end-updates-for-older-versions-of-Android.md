---
layout: post
title: "Google Play Services will end updates for older versions of Android"
author: jane 
date: 09-07-2021 11:57:09 +05:30 
categories: [ BUSINESS ] 
image: assets/images/09-07-2021/Android-Jelly-Bean-Logo.jpg
---
Google Play Services will end updates for older versions of Android

Google Play Services is a library found on all Google-certified Android devices, which powers the Play Store and dozens of APIs for applications that third-party apps can use. Play Services also serves as a conduit for Google to push new features to older versions of Android, like the Nearby Share functionality that recently arrived on all Android 6.0+ devices. However, a few very old phones and tablets won’t receive new Play Services updates moving forward.

Google announced today in a blog post that it will no longer update Google Play Services on Android Jelly Bean, which includes versions 4.1-4.3 (API levels 16, 17, and 18). Google says the older operating systems are being dropped because Jelly Bean now represents less than 1% of active Android users. The final release for devices with Jelly Bean will be Play Services v21.30.99, which is expected to arrive at the end of August. The current latest version of the app is 21.24.18.

“The functionality required by the current SDK versions,” Google said, “is already present on [Jelly Bean] devices with Google Play services and will continue to work without change.” Developers using the Play Services SDK in their apps are recommended to use API level 19 (Android 4.4 KitKat) as the minimum supported API level to avoid issues. It’s also possible for developers to compile multiple APKs, with each APK containing a different version of the Play Services library, if they need to maintain support for Jelly Bean devices.

Android 4.1 Jelly Bean was first released in July 2012, with features like expandable notifications, USB audio, and a smoother interface. Android 4.2 arrived in November 2012 with lock screen improvements and multiple user account support, and Android 4.3 was released in July 2013 with Bluetooth LE and a reworked camera app.