---
title: Java Multiplayer Card Game ‘Gyeol! Hap!’
summary: A real-time multiplayer card game built with Java Swing + Sockets. Includes chat, answer validation, and server/client frames.
type: project
tags:
  - WEB
date: 2024-12-20
draft: false
featured: false
share: false

image:
  filename: projects/java-set-cover.jpg   # static/media/projects/java-set-cover.jpg
  preview_only: false

links:
  - icon: file-archive
    icon_pack: fas
    name: Full Source ZIP
    url: /files/projects/java-set/java-set-source.zip

  - icon: file-word
    icon_pack: fas
    name: Project Report
    url: /files/projects/java-set/project-report.pdf
---

<style>
  .article-style p,
  .article-style li {
    text-align: justify;
  }
</style>

## Project Overview
Implemented the multiplayer card game *“Gyeol! Hap!”* using **Java Swing UI** and **TCP socket communication**.  
Features include real-time chat, server-side answer validation, client UI/event handling, and round management.

### Key Features
- Server/Client architecture (multi-connection, real-time broadcasting)
- Chat and game event messaging protocol
- Java Swing–based game board/control UI
- Server-side answer validation logic and round management

### Roles (Summary)
- **Kang Juhyeon (self):** Overall frame & client (UI) design, image asset creation  
- **Teammates:** `StartFrame`, multiplayer/server implementation, feedback and stabilization