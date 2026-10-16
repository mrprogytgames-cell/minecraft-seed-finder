# 🎮 Minecraft Overpowered Speedrun Seed Finder

⚡ Find the perfect Minecraft seed for speedrunning — automatically.

A Python script that leverages the `cubiomespi` library to find perfect Minecraft (version 1.20) seeds for speedrunning.

---

## ✨ Features

- 🔍 Scans millions of random seeds automatically
- 🏡 Finds 4 key structures within 500 blocks of spawn
- 🌊 Filters out ocean spawns
- ⚡ Fast — powered by the Cubiomes C library
- 🖥️ Cross-platform: Windows, macOS, Linux
- 🆓 100% free and open source

---

## 🎯 Target Structures

| Icon | Structure | Why it matters |
|------|-----------|----------------|
| 🏡 | Village | Loot, beds, food |
| 🌌 | Ruined Portal | Fast Nether entry |
| 🏜️ | Desert Pyramid | Rare loot, TNT |
| ⛏️ | Mineshaft | Ores, cave access |

---

## 📦 Installation & Usage

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the finder:

```bash
python main.py
```

Wait for the magic — the script will print the first matching seed.

> 💡 **Note:** The original `cubiomespi` package supports versions from `MC_1_0_0` up to `MC_1_20`. It installs as a prebuilt wheel — **no C compiler required**. The `cubiomespi-fork` package adds `MC_1_21` support but requires a C compiler.

---

## ⚙️ How It Works

1. Picks a random 64-bit seed
2. Uses `cubiomespi` to simulate world generation
3. Checks if all 4 structures are within 500 blocks of spawn
4. Rejects ocean spawns
5. Returns the first valid seed and stops

---

## 🇷🇺 Русский

# 🎮 Minecraft Overpowered Speedrun Seed Finder

⚡ Находит идеальный сид для спидрана Minecraft — автоматически.

Python-скрипт на базе библиотеки `cubiomespi` для поиска идеальных сидов Minecraft (версия 1.20) для спидранов.

### ✨ Возможности

- 🔍 Автоматически перебирает миллионы случайных сидов
- 🏡 Находит 4 ключевые структуры в радиусе 500 блоков от спавна
- 🌊 Отсеивает спавн посреди океана
- ⚡ Быстро — благодаря C-библиотеке Cubiomes
- 🖥️ Кроссплатформенно: Windows, macOS, Linux
- 🆓 Полностью бесплатно и с открытым кодом

### 🎯 Целевые структуры

| Иконка | Структура | Зачем нужна |
|--------|-----------|-------------|
| 🏡 | Деревня | Лут, кровати, еда |
| 🌌 | Разрушенный портал | Быстрый вход в Незер |
| 🏜️ | Пустынный храм | Редкий лут, ТНТ |
| ⛏️ | Шахта | Руды, доступ к пещерам |

### 📦 Установка и запуск

Установи зависимости:

```bash
pip install -r requirements.txt
```

Запусти скрипт:

```bash
python main.py
```

Жди результата — скрипт выведет первый подходящий сид.

> 💡 **Примечание:** Оригинальный пакет `cubiomespi` поддерживает версии от `MC_1_0_0` до `MC_1_20`. Устанавливается как готовый wheel — **компилятор C не нужен**. Пакет `cubiomespi-fork` добавляет поддержку `MC_1_21`, но требует компилятор C.

### ⚙️ Как это работает

1. Берётся случайный 64-битный сид
2. `cubiomespi` симулирует генерацию мира
3. Проверяется, что все 4 структуры в радиусе 500 блоков от спавна
4. Отсеиваются спавны в океане
5. Возвращается первый подходящий сид, скрипт останавливается

---

## 🇪🇸 Español

# 🎮 Minecraft Overpowered Speedrun Seed Finder

⚡ Encuentra la semilla perfecta de Minecraft para speedrunning — automáticamente.

Script de Python basado en la librería `cubiomespi` para encontrar semillas perfectas de Minecraft (versión 1.20) para speedrunning.

### ✨ Características

- 🔍 Escanea millones de semillas aleatorias automáticamente
- 🏡 Encuentra 4 estructuras clave dentro de 500 bloques del spawn
- 🌊 Descarta spawns en medio del océano
- ⚡ Rápido — gracias a la librería C Cubiomes
- 🖥️ Multiplataforma: Windows, macOS, Linux
- 🆓 100% gratis y de código abierto

### 🎯 Estructuras objetivo

| Icono | Estructura | Por qué importa |
|-------|-----------|-----------------|
| 🏡 | Aldea | Loot, camas, comida |
| 🌌 | Portal en ruinas | Entrada rápida al Nether |
| 🏜️ | Pirámide del desierto | Loot raro, TNT |
| ⛏️ | Mina | Minerales, acceso a cuevas |

### 📦 Instalación y uso

Instala las dependencias:

```bash
pip install -r requirements.txt
```

Ejecuta el script:

```bash
python main.py
```

Espera el resultado — el script imprimirá la primera semilla válida.

> 💡 **Nota:** El paquete original `cubiomespi` soporta versiones desde `MC_1_0_0` hasta `MC_1_20`. Se instala como wheel precompilado — **no requiere compilador de C**. El paquete `cubiomespi-fork` añade soporte para `MC_1_21`, pero requiere un compilador de C.

### ⚙️ Cómo funciona

1. Toma una semilla aleatoria de 64 bits
2. `cubiomespi` simula la generación del mundo
3. Comprueba que las 4 estructuras estén dentro de 500 bloques del spawn
4. Descarta spawns en el océano
5. Devuelve la primera semilla válida y se detiene

---

## 🇩🇪 Deutsch

# 🎮 Minecraft Overpowered Speedrun Seed Finder

⚡ Finde den perfekten Minecraft-Seed für Speedruns — automatisch.

Ein Python-Skript auf Basis der `cubiomespi`-Bibliothek, um perfekte Minecraft-Seeds (Version 1.20) für Speedruns zu finden.

### ✨ Funktionen

- 🔍 Durchsucht automatisch Millionen zufälliger Seeds
- 🏡 Findet 4 Schlüsselstrukturen innerhalb von 500 Blöcken um den Spawn
- 🌊 Filtert Ozean-Spawns heraus
- ⚡ Schnell — dank der Cubiomes-C-Bibliothek
- 🖥️ Plattformübergreifend: Windows, macOS, Linux
- 🆓 100% kostenlos und Open Source

### 🎯 Zielstrukturen

| Icon | Struktur | Warum wichtig |
|------|----------|---------------|
| 🏡 | Dorf | Loot, Betten, Essen |
| 🌌 | Ruiniertes Portal | Schneller Nether-Einstieg |
| 🏜️ | Wüstentempel | Seltener Loot, TNT |
| ⛏️ | Mine | Erze, Höhlenzugang |

### 📦 Installation und Verwendung

Abhängigkeiten installieren:

```bash
pip install -r requirements.txt
```

Skript starten:

```bash
python main.py
```

Auf das Ergebnis warten — das Skript gibt den ersten passenden Seed aus.

> 💡 **Hinweis:** Das ursprüngliche `cubiomespi`-Paket unterstützt Versionen von `MC_1_0_0` bis `MC_1_20`. Es wird als vorkompiliertes Wheel installiert — **kein C-Compiler erforderlich**. Das Paket `cubiomespi-fork` fügt `MC_1_21`-Unterstützung hinzu, benötigt aber einen C-Compiler.

### ⚙️ Wie es funktioniert

1. Wählt einen zufälligen 64-Bit-Seed
2. `cubiomespi` simuliert die Weltgenerierung
3. Prüft, ob alle 4 Strukturen innerhalb von 500 Blöcken um den Spawn liegen
4. Verwirft Ozean-Spawns
5. Gibt den ersten gültigen Seed zurück und stoppt

---

## 🇨🇳 中文

# 🎮 Minecraft Overpowered Speedrun Seed Finder

⚡ 自动寻找完美的 Minecraft 速通种子。

一个基于 `cubiomespi` 库的 Python 脚本，用于寻找适合速通的完美 Minecraft 种子（版本 1.20）。

### ✨ 功能

- 🔍 自动扫描数百万个随机种子
- 🏡 在出生点 500 格范围内找到 4 种关键结构
- 🌊 过滤掉海洋中的出生点
- ⚡ 快速 — 由 Cubiomes C 库驱动
- 🖥️ 跨平台：Windows、macOS、Linux
- 🆓 100% 免费且开源

### 🎯 目标结构

| 图标 | 结构 | 重要性 |
|------|------|--------|
| 🏡 | 村庄 | 战利品、床、食物 |
| 🌌 | 废弃传送门 | 快速进入下界 |
| 🏜️ | 沙漠神殿 | 稀有战利品、TNT |
| ⛏️ | 废弃矿井 | 矿石、洞穴入口 |

### 📦 安装与使用

安装依赖：

```bash
pip install -r requirements.txt
```

运行脚本：

```bash
python main.py
```

等待结果 — 脚本会输出第一个符合条件的种子。

> 💡 **注意：** 原始的 `cubiomespi` 包支持从 `MC_1_0_0` 到 `MC_1_20` 的版本。它以预编译 wheel 形式安装——**无需 C 编译器**。`cubiomespi-fork` 包增加了对 `MC_1_21` 的支持，但需要 C 编译器。

### ⚙️ 工作原理

1. 随机选择一个 64 位种子
2. `cubiomespi` 模拟世界生成
3. 检查 4 种结构是否都在出生点 500 格范围内
4. 排除海洋出生点
5. 返回第一个符合条件的种子并停止

---

## 👤 Author

<p align="center">
  <a href="https://www.youtube.com/@potha3amokofficial"><img src="https://img.shields.io/badge/YouTube-FF0000?style=for-the-badge&logo=youtube&logoColor=white" /></a>
  <a href="https://www.tiktok.com/@potha3amokofficial"><img src="https://img.shields.io/badge/TikTok-000000?style=for-the-badge&logo=tiktok&logoColor=white" /></a>
  <a href="https://steamcommunity.com/id/POTHA3AMOK/"><img src="https://img.shields.io/badge/Steam-171A21?style=for-the-badge&logo=steam&logoColor=white" /></a>
  <a href="https://t.me/potha3amokYT"><img src="https://img.shields.io/badge/Telegram-26A5E4?style=for-the-badge&logo=telegram&logoColor=white" /></a>
  <a href="https://discord.gg/psK8T9NFzQ"><img src="https://img.shields.io/badge/Discord-5865F2?style=for-the-badge&logo=discord&logoColor=white" /></a>
  <a href="https://github.com/mrprogytgames-cell"><img src="https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white" /></a>
</p>
