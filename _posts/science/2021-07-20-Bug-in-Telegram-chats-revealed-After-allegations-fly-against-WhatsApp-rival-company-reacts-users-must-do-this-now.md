---
layout: post
title: "Bug in Telegram chats revealed? After allegations fly against WhatsApp rival, company reacts; users must do this now"
author: jane 
date: 20-07-2021 15:32:44 +05:30 
categories: [ TECHNOLOGY ] 
image: assets/images/20-07-2021/367553776_0-7_1613144463298_1613144484240_1626613623228.jpg
---
Telegram users have received a big shock. The messaging app that is touted as an alternative to WhatsApp, has reportedly had to patch up security vulnerabilities, according to a group of researchers at the Royal Holloway, University of London. Telegram platform offers opt-in end-to-end encryption (E2EE) which users can turn on for individual chats, but the service offers non-E2EE chats by default. According to the researchers, the bug discovered on the Telegram app was connected to the technology used to protect the second type of chats mentioned above.

What is End-to-end encryption?

End-to-end encryption (E2EE) refers to the technology used to protect the contents of a chat to prevent anyone but the sender and recipients from seeing. Apps that offer E2EE encryption protect chats in such a way that the chats cannot be read by the companies concerned either – WhatsApp and Signal enable this by default. Apps like Telegram, Skype, and Facebook Messenger do offer a form of E2EE chats, but they have to be manually turned on, failing which the apps can read all the users chats. One big advantage of E2EE chats are that users are protected from Man in the Middle (MITM) attacks, where a person or group is able to read the chats in a group.

Together with Lenka Mareková, @kennyog and Igors Stepanovs, we took a deep dive into @telegram’s symmetric cryptography: “Four Attacks and a Proof for Telegram” to be presented at @IEEESSP 2022. https://t.co/60sSPD07Hq 🧵 by @kennyog and me: pic.twitter.com/jn5P72kWS9 — Martin R. Albrecht (@martinralbrecht) July 16, 2021

What did the researchers discover?

According to the researchers, the messaging app’s non E2EE chats suffered from a bug that could allow an attacker to change the order of messages on the app. For example, if a user wrote “I say yes” and “to pizza” and “I say no” with “to crime” then the attackers could possibly rearrange the messages to say “I say yes to crime”.

In fact, the vulnerability could be used to manipulate “bots” on Telegram, the report said. Bots are automated systems on Telegram that can be used in groups to automate tasks like moderating groups. Similarly, the researchers also found that attackers could extract the chats in readable form from encrypted messages on the apps for iOS, Android and the Telegram desktop apps. However, the report states that such an attack would need to be carried out by a significant adversary, such as attackers backed by a nation-state.

What did Telegram have to say about the issue?

A Telegram blog post on July 16 explained that the company had already fixed the security flaws related to the app. “The latest versions of official Telegram apps already contain the changes that make the four observations made by the researchers no longer relevant. Overall, none of the changes were critical, as no ways of deciphering or tampering with messages were discovered,” the company stated on the blog post. The researchers had responsibly disclosed the vulnerabilities to Telegram in advance to allow them to fix the issues before they were disclosed.

What can users do?

As Telegram has fixed the bugs with their apps, users should not be affected as long as they have updated to the latest version of the app on their devices. Users can head over to the Google Play Store, the Apple App Store or the official Telegram website to download the updated version of the messaging app for their devices.

Alternatively, they can go and download the always-on, end-to-end encrypted messenger Signal to keep their messages safe and secure so only the intended recipients can view them.