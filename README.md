<h1 align="center">
  <img src="logo.png" width="20%" height="30%" style="vertical-align: middle;" alt="Payloadility logo">
</h1>

<p align="center">
  <img src="https://readme-typing-svg.demolab.com/?lines=Payloadility;&font=Fira%20Code&center=true&width=380&height=50&duration=4000&pause=1000" alt="Payloadility">
</p>

# ⚡ Payloadility — Security Payload Generator

[![Python 3.8+](https://img.shields.io/badge/Python-3.8%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)](LICENSE)
[![Platform: Linux](https://img.shields.io/badge/Platform-Linux-FCC624?style=for-the-badge&logo=linux&logoColor=black)](#-installation--global-setup)

**Payloadility** is a lightweight, dependency-free Python CLI for generating controlled security-testing payloads. It provides one consistent interface for selecting, filtering, sampling, and encoding payloads for common web-application vulnerability classes.

Full Breakdown: https://medium.com/@qasimovdavud39/payloadility-a-lightweight-payload-generator-for-authorized-security-testing-ec80d8c4999d?sharedUserId=qasimovdavud39

Payloadility is a **payload-generation utility**, not an exploitation framework. It does not scan targets, send HTTP requests, execute payloads, bypass authentication, or perform brute-force activity.

> Use Payloadility only against systems that you own or are explicitly authorized to test.

---

## 🚀 Key Features

* **Unified CLI Syntax:** One command style for all supported payload categories.
* **50+ Payloads per Category:** XSS, SQLi, LFI, SSTI, command injection, XXE, and open redirect.
* **Random Selection:** Print a limited random sample with `--count`.
* **Payload Filtering:** Search payload content with `--search`.
* **Encoding Modes:** Plain, URL, double URL, and HTML escaping.
* **No Third-Party Dependencies:** Uses only the Python standard library.
* **Readable Output:** One payload per line, suitable for terminal use or shell redirection.

## 🧰 Supported Categories

| Category | CLI name | Purpose |
|---|---|---|
| Cross-Site Scripting | `xss` | HTML, attribute, event-handler, and DOM-context test strings. |
| SQL Injection | `sqli` | Syntax, boolean, error, ordering, timing, and union-oriented probes. |
| Local File Inclusion | `lfi` | Unix, Windows, traversal, wrapper, and normalization probes. |
| Server-Side Template Injection | `ssti` | Arithmetic and template-expression detection strings. |
| Command Injection | `command-injection` | Unix and Windows command-separator test strings. |
| XML External Entity | `xxe` | XML entity and local-resource reference test definitions. |
| Open Redirect | `open-redirect` | URL-parser and redirect-validation test strings. |

## 🛠️ Prerequisites

* Python 3.8 or newer.
* Linux, macOS, or Windows with a terminal.
* No additional Python packages are required.

## 📥 Installation & Global Setup

To run **Payloadility** as a system-wide command from any directory in your terminal:

### 1. Clone the Repository & Set Execution Permissions

```bash
git clone [https://github.com/DavudQasimov/Payloadility.git](https://github.com/DavudQasimov/Payloadility.git)
cd Payloadility
chmod +x payloadility.py
```

If the project is already downloaded:

```bash
cd /path/to/Payloadility
chmod +x payloadility.py
```

### 2. Create a Global Symbolic Link

Create a symbolic link in `/usr/local/bin` so the operating system recognizes the command globally:

```bash
# Register as 'payloadility'
sudo ln -s "$(pwd)/payloadility.py" /usr/local/bin/payloadility
```

If a link already exists, replace it with:

```bash
sudo ln -sf "$(pwd)/payloadility.py" /usr/local/bin/payloadility
```

### 3. Verify Installation

Open a new terminal shell, or refresh the zsh command cache:

```bash
rehash 2>/dev/null || true
payloadility --help
payloadility 
```

You can now run Payloadility from any directory:

```bash
cd /tmp
payloadility xss --count 5
```

### 4. Make Global Installation Persistent

The symbolic link remains available after closing the terminal. The source file must remain at the path used when creating the link.

To verify the installation:

```bash
command -v payloadility
ls -l "$(command -v payloadility)"
```

For a standalone copy outside the source directory:

```bash
sudo install -D -m 755 payloadility.py /usr/local/lib/payloadility/payloadility.py
sudo ln -sfn /usr/local/lib/payloadility/payloadility.py /usr/local/bin/payloadility
rehash 2>/dev/null || true
payloadility --help
```

To uninstall the global launcher:

```bash
sudo rm -f /usr/local/bin/payloadility
sudo rm -rf /usr/local/lib/payloadility
rehash 2>/dev/null || true
```

## 📖 CLI Argument Reference

```text
usage: payloadility.py [-h]
                       [--encode {none,url,double-url,html}]
                       [--count COUNT] [--search TEXT] [--list]
                       [--no-banner]
                       [{command-injection,lfi,open-redirect,sqli,ssti,xss,xxe}]
```

### Positional argument

| Argument | Required | Description |
|---|---:|---|
| `CATEGORY` | No | Selects the payload category to print. |

### Options

| Flag / Option | Type | Description |
|---|---|---|
| `-h`, `--help` | Flag | Displays the complete built-in help message and exits. |
| `--list` | Flag | Lists all categories and the number of available payloads. |
| `--encode {none,url,double-url,html}` | Choice | Selects the output transformation. Default: `none`. |
| `--count COUNT` | Integer | Prints up to `COUNT` randomly selected payloads. |
| `--search TEXT` | String | Prints only payloads containing `TEXT`, case-insensitively. |
| `--no-banner` | Flag | Suppresses the ASCII banner for clean output and pipelines. |

`--count` is applied after `--search`, so you can filter first and randomly select from matching results.

### Encoding Modes

| Mode | Explanation |
|---|---|
| `none` | Prints the payload unchanged. |
| `url` | Applies URL percent-encoding once. |
| `double-url` | Applies URL percent-encoding twice. |
| `html` | Escapes HTML-sensitive characters such as `<`, `>`, quotes, and `&`. |

## 📊 Payload Coverage

Every requested category contains at least 50 payloads:

| Category | Count |
|---|---:|
| XSS | 57 |
| SQLi | 63 |
| LFI | 54 |
| SSTI | 52 |
| Command Injection | 54 |
| XXE | 54 |
| Open Redirect | 55 |

Counts may increase as the payload database is expanded. Payloadility only prints these strings; it does not send or execute them.

## 🧪 Recommended Authorized Workflow

1. Obtain written authorization and define the target scope.
2. Identify the input context being assessed.
3. Select the relevant Payloadility category.
4. Start with `--search` and a small `--count` value.
5. Apply encoding only when it matches the intended test path.
6. Record the test input, response behavior, and remediation evidence.
7. Stop immediately if the test exceeds the approved scope.

## ⚠️ Disclaimer

Payloadility is designed strictly for authorized penetration testing, secure-development validation, laboratory exercises, and defensive research. Unauthorized testing may be illegal. The author assumes no liability for misuse, service disruption, data loss, or damage caused by this software.

## 👤 Author & Contact
**Davud Qasimov**

* LinkedIn: [Davud Qasimov](https://www.linkedin.com/in/davud-qasimov-798928303/)
* Medium: [qasimovdavud39](https://medium.com/@qasimovdavud39)
* Gmail: [qasimovdavud39@gmail.com](mailto:qasimovdavud39@gmail.com)
* Discord: `etozryx_13553`

## 📄 License

Released under the MIT License. See [`LICENSE`](LICENSE).
