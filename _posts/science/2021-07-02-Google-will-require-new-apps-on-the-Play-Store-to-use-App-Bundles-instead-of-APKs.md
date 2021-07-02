---
layout: post
title: "Google will require new apps on the Play Store to use App Bundles instead of APKs"
author: jane 
date: 02-07-2021 12:13:53 +05:30 
categories: [ TECHNOLOGY ] 
image: assets/images/02-07-2021/gsmarena_000.jpg
---
Lines are being drawn in the sand – starting in August, Google will require that new apps listed on its Play Store are published in the Android App Bundle (AAB) format, instead of the APK format that has been a part of the OS since its inception.

Why does that matter? Well, right now only the Google Play Store supports App Bundles. That’s right, the Amazon Appstore, which will be the default Android app store on Windows 11 does not. And neither do the third-party app stores that will be natively supported in the upcoming Android 12 update.

Google, of course, touts App Bundles as an upgrade. The format was introduced back in 2018 and is a way to deliver smaller updates to users. The Play servers can figure out what language, image resolution and additional resources are needed for your specific device and creates an optimized APK just for you (normally, an APK has to work on a variety of devices and includes resources you don’t need).

You can jump to the 2 minute mark of this video for a simple overview of APK vs. bundles (or watch the whole thing for more details, though it’s a bit techy):

Some of the more interesting features enabled by Bundles is that an app can be split into pieces. Imagine a game, many who try it will not make it past the first level – so why download all the assets for the final boss? With Play Asset Delivery, those later levels can be downloaded only when needed. And the Play Store will figure out which assets are best for your device, e.g. no need for high resolution textures on a low-end device, which will further cut down data transfer requirements.

Naturally, the App Bundle format is open source, so other stores can adopt it. Many developers already use it – the majority of the top 1,000 apps on Play are Bundles. In total, over 1 million apps are available in the Bundle format. Building both an APK and an Android App Bundle isn’t a difficult process either, it’s just a few clicks away on the major tools (e.g. Android Studio, Unity, Unreal Engine and others).

And this only affects new apps, anyway, existing apps can continue to deliver updates as APKs. Here is a summary of what is about to change:

TYPE OF RELEASE REPLACED REQUIRED AUG 2021 New apps on Google Play APK Android App Bundle (AAB) Expansion files (OBBs) Play Asset Delivery or Play Feature Delivery Updates to existing apps No change New instant experiences Instant app ZIP Instant-enabled Android App Bundle (AAB) Updates to instant experiences

So, the switch to Bundles will not starve out competing app stores. But it does make it clear which is the One True App Store for Android (as if moving core functionality to Google Play Services didn’t already make it clear).

Source