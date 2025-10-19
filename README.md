# 🛡️ Active Directory Security Lab - Attack & Defense Simulation

An interactive web-based cybersecurity training platform that simulates common Active Directory attacks and demonstrates detection mechanisms. Built for educational purposes to help security professionals understand AD attack vectors and defensive strategies.

![License](https://img.shields.io/badge/license-MIT-blue.svg)
![Python](https://img.shields.io/badge/python-3.8+-blue.svg)
![Flask](https://img.shields.io/badge/flask-3.0.0-green.svg)

## 🎯 Project Overview

This project provides hands-on experience with Active Directory security concepts through realistic attack simulations and corresponding detection mechanisms. Perfect for cybersecurity students, aspiring security analysts, and IT professionals learning about enterprise security.

### ⚠️ Educational Purpose Disclaimer

**This tool is designed exclusively for educational purposes.** All attacks are simulations that do not target real systems. Users are responsible for ensuring they only use this tool in authorized environments for learning purposes.

## ✨ Features

### 🔴 Attack Simulations

1. **Password Spraying**
   - Simulate testing multiple accounts with common passwords
   - View success rates and detection patterns
   - Learn about account lockout policies

2. **Kerberoasting**
   - Extract and crack service account TGS tickets
   - Understand Kerberos authentication weaknesses
   - See hash cracking simulations

3. **Pass-the-Hash**
   - Simulate NTLM hash extraction and reuse
   - Demonstrate lateral movement techniques
   - Understand credential theft impacts

4. **Golden Ticket**
   - Simulate KRBTGT account compromise
   - Create forged Kerberos tickets
   - Demonstrate domain persistence techniques

### 🔵 Detection & Defense

- **Real-time Detection Events**: See how attacks trigger security alerts
- **Detection Logic**: Understand what patterns indicate malicious activity
- **Mitigation Recommendations**: Learn best practices for each attack type
- **Attack Logs**: Complete audit trail of all simulated activities
- **Environment Monitoring**: Track domain health and status

### 📊 Interactive Dashboard

- Real-time attack visualization
- Security event correlation
- Comprehensive logging system
- Professional cybersecurity-themed UI
- Mobile-responsive design

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- pip (Python package installer)
- Modern web browser

### Installation

1. **Clone the repository**
```bash
git clone https://github.com/TheGhostPacket/ad-security-lab.git
cd ad-security-lab
```

2. **Create a virtual environment** (recommended)
```bash
python -m venv venv

# On Windows
venv\Scripts\activate

# On macOS/Linux
source venv/bin/activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Run the application**
```bash
python app.py
```

5. **Access the application**
Open your browser and navigate to:
```
http://localhost:5000
```

## 📁 Project Structure

```
ad-security-lab/
│
├── app.py                  # Main Flask application
├── requirements.txt        # Python dependencies
├── README.md              # Project documentation
│
├── templates/
│   └── index.html         # Main dashboard interface
│
└── static/               # Static assets (if needed)
```

## 🎓 Educational Value

### What You'll Learn

- **Active Directory Architecture**: Understand domain structure and authentication
- **Attack Techniques**: Learn real-world AD exploitation methods
- **Detection Strategies**: Identify malicious patterns and indicators
- **Security Best Practices**: Implement effective defensive measures
- **MITRE ATT&CK Framework**: Map attacks to industry-standard framework

### Perfect For

- 🎓 Cybersecurity students
- 💼 Aspiring security analysts
- 🔒 IT professionals learning AD security
- 📚 Security+ certification preparation
- 🏢 SOC team training
- 🎯 Penetration testing education

## 🔧 Technical Stack

- **Backend**: Python Flask
- **Frontend**: HTML5, CSS3, JavaScript
- **Architecture**: Single-page application (SPA)
- **Deployment**: Works locally or on cloud platforms

## 📈 Future Enhancements

- [ ] Additional attack scenarios (DCSync, AdminSDHolder)
- [ ] Custom attack parameter configuration
- [ ] Export reports to PDF
- [ ] Integration with SIEM platforms
- [ ] Multi-tenant support for classroom use
- [ ] Scoring system for training exercises
- [ ] API endpoints for automation

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request. For major changes, please open an issue first to discuss what you would like to change.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## ⚖️ Legal Notice

This tool is provided for educational and research purposes only. Users must:
- Only use in authorized environments
- Comply with all applicable laws and regulations
- Not use for malicious purposes
- Understand they are solely responsible for their actions

The author assumes no liability for misuse of this software.

## 👨‍💻 Author

**TheGhostPacket**
- Portfolio: [theghostpacket.com](https://theghostpacket.com)
- GitHub: [@TheGhostPacket](https://github.com/TheGhostPacket)
- LinkedIn: [Nhyira Yanney](https://www.linkedin.com/in/nhyira-yanney-b19898178)
- Email: contact@theghostpacket.com

## 🙏 Acknowledgments

- Inspired by real-world Active Directory security challenges
- Built for the cybersecurity education community
- Thanks to all security researchers sharing knowledge

## 📚 Resources

Learn more about Active Directory security:
- [MITRE ATT&CK - Active Directory](https://attack.mitre.org/)
- [Microsoft Active Directory Security](https://docs.microsoft.com/en-us/windows-server/identity/ad-ds/plan/security-best-practices/best-practices-for-securing-active-directory)
- [SANS Active Directory Security](https://www.sans.org/blog/)

---

**⭐ If you find this project helpful, please consider giving it a star!**

Made with ❤️ for the cybersecurity community
