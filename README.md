# Real-Time FinTech Portfolio Risk & Trading Dashboard

An automated quantitative finance application designed to track, calculate, and evaluate live equity portfolios. This tool interfaces directly with live exchange market data feeds to compute real-time profit-and-loss matrices, portfolio asset weight allocations, and net investment summaries.

## 🚀 The Quantitative Profile

This repository serves as a foundational capstone project bridging tech, advanced risk metrics, and financial logic:
* **Academic Track:** B.Tech in Computer Science and Business Systems (CSBS) at VIT-AP.
* **Core Risk Foundations:** Active Actuarial Science track focusing on probability theory, life contingencies, and financial mathematics.
* **Data Infrastructure:** Certified Foundational Data Science tracks via IIT Madras.

---

## 🛠️ Key Architectural Features

* **Live Market Streaming:** Integrated via the `yfinance` API to stream real-time prices directly from the National Stock Exchange (NSE).
* **Data Processing Layer:** Built utilizing `pandas` data frames to manage multi-asset portfolio matrix transformations.
* **Resilient Architecture:** Embedded custom error-handling pipelines to gracefully handle empty data frames, server timeouts, or delisted assets without system crashes.
* **Automated Financial Formatting:** Programmed explicit structural layouts using native local currency string formatting symbols (₹) and dynamic numeric precision limits (+/- .2f).

---

## 📊 Core Financial Equations Implemented

The tracking dashboard calculates sequential investment steps using standard corporate finance methodologies:

1. **Initial Position Capital Outlay:**
   $$\text{Initial Cost} = \sum (\text{Shares Bought} \times \text{Purchase Price})$$

2. **Real-Time Portfolio Equity Valuation:**
   $$\text{Current Market Value} = \sum (\text{Shares Owned} \times \text{Live Market Price})$$

3. **Asset-Specific Realized Return Matrix:**
   $$\text{Return Percentage (\%)} = \left( \frac{\text{Current Value} - \text{Initial Cost}}{\text{Initial Cost}} \right) \times 100$$

---

## 💻 Tech Stack & Engineering Environment

* **Language:** Python 3.14+
* **Data Engines:** Pandas, NumPy
* **API Providers:** Yahoo Finance (`yfinance`)
* **Environment toolchain:** VS Code, Git, UV Package Manager

---

## 📈 Planned Strategic Roadmap

- [ ] **Phase 2:** Integrate an active `ExchangeRate-API` to handle global currency conversions seamlessly (INR/USD/EUR).
- [ ] **Phase 3:** Embed a live 10-second automatic terminal refresh and clear loop via `time.sleep()`.
- [ ] **Phase 4 (Actuarial Addition):** Build a Historical Simulation Value-at-Risk (VaR) module to forecast maximum portfolio downside risk limits at a 95% confidence parameter.
-