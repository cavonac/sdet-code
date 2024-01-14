# sdet-code
This repo should be located at [https://github.com/cavonac/sdet-code.git](https://github.com/cavonac/sdet-code.git)

The purpose of this repository is to provide a novice **software development engineer in test** (SDET) with content for self-studying programming and data langauges. SDETs have a hybrid skillset which includes testing, programming (or software development), DevOps, and database administration. SDETs typically create test automation to improve the development-test-release software cycle.

## In This Repo

| Link | Description |
| ---- | ----------- |
| .gitignore | A gitignore file specifies intentionally untracked files that Git should ignore. This is useful for keeping local copies of config files for modification between environments or clients.
| README.md | You can add a README file to a repository to communicate important information about your project. A README communicates expectations for your project and helps you manage contributions.
[SQL Learning Notebook](SqlLearning.ipynb) | Example SQL queries to understand and possibly execute with some setup required.
|[Python - Blockchain](test_blockchain.py) | 
|[Python Programming Notebook](PythonProgramming.ipynb) | Python notebook with example definitions (sames as methods, functions, operations, etc.) for various tasks along with some sample PyTests.
| [Python - Fibonacci](test_fibonacci.py) | Sample Python code to create and verify numbers of the Fibonacci sequence
| [Python - String Challenge](test_string_challenges.py) | Example linear search algorithm and test cases
| [Python - Web Requests](test_web_requests.py) | First look at real-world testing for OWASP recommended headers on owasp.org

## Recommended Links
| Link | Description |
| ---- | ----------- |
| [Python.com](https://www.python.org/) | Python is a programming language that lets you work more quickly and integrate your systems more effectively. Some data structures include <i>lists</i>, <i>dictionaries</i>, <i>tuples</i>, and <i>sets</i>. 
| [Python cheatsheet](https://perso.limsi.fr/pointal/_media/python:cours:mementopython3-english.pdf) | Cheatsheet on Python (2 pages). 
| [Download Git](https://git-scm.com/downloads) | Source control management (SCM) application that synchronizes local files and folders with a central remote repository using a modern branching model to create, merge, or delete lines of code in development.
| [Azure Data Studio (ADS)](https://aka.ms/azuredatastudio) | A cross-platform database tool for data professionals using on-premises and cloud data platforms with IntelliSense, code snippets, source control integration, and an integrated terminal. It's engineered with the data platform user in mind, with built-in charting of query result sets and customizable dashboards. 
| [Download Visual Studio Code (Code)](https://code.visualstudio.com/Download) | Visual Studio Code is a streamlined code editor with support for development operations like debugging, task running, and version control. 
| |![](img/code.png)
| [GitHub Desktop](https://desktop.github.com) | Simplifies your development workflow using Git
| | ![](img/ghd.png)
| [Git Cheatsheet](https://training.github.com/downloads/github-git-cheat-sheet/) | Refer to the basic Git commands used often
|[SQL Server Central](https://www.sqlservercentral.com/articles/getting-comfortable-writing-code-in-azure-data-studio) | Getting comfortable writing code in Azure Data Studio
| [Markdown Syntax](https://www.markdownguide.org/basic-syntax) | Guide for authoring text using markdown (like this README.md file)
| [PyTest](https://www.pytest.org/) | To use, run 'pytest' from a command line and it should automatically find tests and run them from console. Installation may be required: <code>pip install -U pytest</code>. 
| [OWASP](https://owasp.org) | Open Web Application Security Project is a nonprofit foundation that works to improve the security of software.

## Blockchain Example
Proof-of-Work (PoW) is a consensus algorithm used in blockchain networks to achieve distributed consensus and secure the network against malicious activities. The primary purpose of PoW is to ensure that participants (often referred to as miners) in the network invest computational power to validate transactions and add new blocks to the blockchain. Here's an explanation of how the PoW algorithm typically works:

1. **Mining Process:**
   - Participants in the network (miners) compete to solve a complex mathematical problem.
   - The problem is computationally intensive and requires significant processing power to solve.

2. **Difficulty Level:**
   - The network adjusts the difficulty of the problem regularly to maintain a consistent block creation time (e.g., in Bitcoin, a new block is targeted to be mined every 10 minutes).
   - As more miners join the network, the difficulty increases to ensure that blocks are not mined too quickly.

3. **Finding the Nonce:**
   - Miners repeatedly modify the block's header by changing a parameter called the "nonce."
   - The nonce is a 32-bit number, and miners iterate through possible values until they find a nonce that, when combined with the block data, produces a hash that meets certain criteria.

4. **Hash Function:**
   - The hash function used (e.g., SHA-256 in Bitcoin) should be fast to compute in one direction but difficult to reverse.
   - Miners aim to find a hash value that is below a specific target or has a certain number of leading zeros.

5. **Validating the Solution:**
   - Once a miner finds a nonce that satisfies the criteria, they broadcast the solution to the network.
   - Other nodes can quickly verify that the hash is correct by using the same nonce and checking if the result meets the required conditions.

6. **Consensus and Block Addition:**
   - If the solution is valid, the miner adds the new block to the blockchain.
   - Other nodes accept the new block, and the consensus mechanism ensures that the majority agrees on the validity of the solution.

7. **Incentives:**
   - Miners are often rewarded with cryptocurrency (e.g., new coins) for successfully mining a block.
   - This incentive system encourages miners to contribute their computational power to secure the network.

8. **Security:**
   - PoW provides security against various attacks like double-spending and Sybil attacks by making it computationally expensive to control the majority of the network's mining power.

It's worth noting that while PoW is effective, it consumes a significant amount of energy. Some blockchain networks are exploring alternative consensus mechanisms, like Proof-of-Stake (PoS), to address environmental concerns. Each consensus algorithm has its trade-offs, and the choice depends on the goals and priorities of a particular blockchain network.

### Kinds of Algorithms
- **Hash Puzzle:** Miners find a special number (nonce) to make the data's hash meet specific criteria.
- **Cryptographic Hash Functions:** Miners solve a puzzle by repeatedly hashing until they find a hash with certain properties.
Finding Prime Numbers: Miners work on problems involving large prime numbers.
- **Integer Factorization:** Miners find the factors of large numbers.
Discrete Logarithm Problem: Miners solve problems related to logarithms in mathematical groups.
- **Graph Theory Problems:** Miners navigate or analyze graph structures.
Random Oracle Model: Miners provide inputs that yield specific outputs from a random oracle.
- **Merkle Tree Proofs:** Miners generate or validate proofs about data in a cryptographic tree.
- **Zero-Knowledge Proofs:** Miners prove knowledge of a secret without revealing it.
- **Lattice-based Cryptography:** Miners work on problems involving mathematical structures called lattices.

# Contributions
Contributing to this repo is welcomed in forms of issues or code. Create a separate branch and merge your code contribution to **main** with a Pull Request.