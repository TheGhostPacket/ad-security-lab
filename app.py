from flask import Flask, render_template, jsonify, request
import random
import time
from datetime import datetime, timedelta
import hashlib

app = Flask(__name__)

# Simulated AD environment data
DOMAIN_USERS = [
    {"username": "john.doe", "department": "IT", "privileged": False},
    {"username": "jane.smith", "department": "HR", "privileged": False},
    {"username": "admin.service", "department": "IT", "privileged": True},
    {"username": "bob.johnson", "department": "Finance", "privileged": False},
    {"username": "alice.williams", "department": "IT", "privileged": True},
    {"username": "charlie.brown", "department": "Sales", "privileged": False},
]

DOMAIN_CONTROLLERS = [
    {"name": "DC01", "ip": "10.0.0.10", "status": "healthy"},
    {"name": "DC02", "ip": "10.0.0.11", "status": "healthy"},
]

# Store attack simulations
attack_logs = []
detection_events = []

def generate_attack_log(attack_type, status, details):
    """Generate attack log entry"""
    log = {
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "attack_type": attack_type,
        "status": status,
        "details": details,
        "source_ip": f"192.168.1.{random.randint(100, 250)}"
    }
    attack_logs.append(log)
    return log

def generate_detection_event(attack_type, severity, message):
    """Generate detection event"""
    event = {
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "attack_type": attack_type,
        "severity": severity,
        "message": message,
        "recommended_action": get_mitigation(attack_type)
    }
    detection_events.append(event)
    return event

def get_mitigation(attack_type):
    """Get mitigation recommendations"""
    mitigations = {
        "password_spray": "Enable account lockout policies, implement MFA, monitor for multiple failed logins",
        "kerberoasting": "Use strong service account passwords, implement Managed Service Accounts, monitor for TGS requests",
        "pass_the_hash": "Disable NTLM authentication, use Credential Guard, implement Privileged Access Workstations",
        "golden_ticket": "Reset KRBTGT account password twice, monitor for anomalous TGT requests, implement PAW"
    }
    return mitigations.get(attack_type, "Implement defense-in-depth security controls")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/environment')
def get_environment():
    """Get current AD environment status"""
    return jsonify({
        "domain": "SECURITY-LAB.LOCAL",
        "users": len(DOMAIN_USERS),
        "domain_controllers": DOMAIN_CONTROLLERS,
        "privileged_accounts": len([u for u in DOMAIN_USERS if u["privileged"]]),
        "status": "healthy"
    })

@app.route('/api/simulate/password-spray', methods=['POST'])
def simulate_password_spray():
    """Simulate password spraying attack"""
    target_users = random.sample(DOMAIN_USERS, 3)
    common_passwords = ["Password123!", "Summer2024!", "Welcome1!", "Company123!"]
    
    results = []
    detected = False
    
    for user in target_users:
        password = random.choice(common_passwords)
        success = random.random() < 0.1  # 10% success rate
        
        result = {
            "username": user["username"],
            "password_tried": password,
            "success": success,
            "timestamp": datetime.now().strftime("%H:%M:%S")
        }
        results.append(result)
        
        if success:
            generate_attack_log(
                "Password Spray",
                "Success",
                f"Successfully authenticated as {user['username']} using password spray"
            )
            detected = True
        
    if detected or len(results) >= 3:
        generate_detection_event(
            "password_spray",
            "HIGH",
            f"Detected password spray attack targeting {len(results)} accounts from same source IP"
        )
    
    return jsonify({
        "success": True,
        "results": results,
        "detected": detected,
        "total_attempts": len(results),
        "detection_triggered": detected or len(results) >= 3
    })

@app.route('/api/simulate/kerberoasting', methods=['POST'])
def simulate_kerberoasting():
    """Simulate Kerberoasting attack"""
    service_accounts = [u for u in DOMAIN_USERS if u["privileged"]]
    target_account = random.choice(service_accounts)
    
    # Simulate TGS-REP request
    ticket_hash = hashlib.md5(f"{target_account['username']}{time.time()}".encode()).hexdigest()
    
    crack_time = random.randint(30, 300)  # seconds
    cracked = random.random() < 0.3  # 30% crack success rate
    
    generate_attack_log(
        "Kerberoasting",
        "In Progress",
        f"Requested TGS ticket for {target_account['username']}"
    )
    
    generate_detection_event(
        "kerberoasting",
        "MEDIUM",
        f"Unusual TGS-REP request pattern detected for service account {target_account['username']}"
    )
    
    result = {
        "target_account": target_account["username"],
        "ticket_extracted": True,
        "ticket_hash": f"$krb5tgs$23${ticket_hash[:32]}...",
        "crack_attempted": True,
        "cracked": cracked,
        "crack_time_seconds": crack_time if cracked else None,
        "password": "ServicePass123!" if cracked else None
    }
    
    if cracked:
        generate_attack_log(
            "Kerberoasting",
            "Success",
            f"Successfully cracked password for {target_account['username']}"
        )
    
    return jsonify(result)

@app.route('/api/simulate/pass-the-hash', methods=['POST'])
def simulate_pass_the_hash():
    """Simulate Pass-the-Hash attack"""
    admin_accounts = [u for u in DOMAIN_USERS if u["privileged"]]
    target_account = random.choice(admin_accounts)
    
    # Simulate NTLM hash extraction
    ntlm_hash = hashlib.md5(f"{target_account['username']}_hash".encode()).hexdigest()
    
    # Simulate lateral movement
    target_systems = [
        "FILE-SERVER-01",
        "APP-SERVER-02", 
        "DATABASE-01",
        "WEB-SERVER-03"
    ]
    
    compromised_systems = random.sample(target_systems, random.randint(2, 4))
    
    generate_attack_log(
        "Pass-the-Hash",
        "Success",
        f"Extracted NTLM hash for {target_account['username']}"
    )
    
    generate_detection_event(
        "pass_the_hash",
        "CRITICAL",
        f"Detected NTLM authentication without Kerberos pre-authentication for {target_account['username']}"
    )
    
    return jsonify({
        "account_compromised": target_account["username"],
        "ntlm_hash": f"{ntlm_hash[:16]}...{ntlm_hash[-16:]}",
        "lateral_movement": True,
        "compromised_systems": compromised_systems,
        "total_systems_accessed": len(compromised_systems),
        "detection_triggered": True
    })

@app.route('/api/simulate/golden-ticket', methods=['POST'])
def simulate_golden_ticket():
    """Simulate Golden Ticket attack"""
    # Simulate KRBTGT hash extraction
    krbtgt_hash = hashlib.sha256(b"krbtgt_account_hash").hexdigest()
    
    # Create fake admin account
    fake_admin = f"fake_admin_{random.randint(1000, 9999)}"
    
    # Simulate ticket creation
    ticket_lifetime = 10 * 365 * 24  # 10 years in hours
    
    generate_attack_log(
        "Golden Ticket",
        "Critical",
        f"KRBTGT account hash extracted - {krbtgt_hash[:32]}..."
    )
    
    generate_detection_event(
        "golden_ticket",
        "CRITICAL",
        "Detected TGT with unusual lifetime and properties. Possible Golden Ticket attack!"
    )
    
    # Simulate domain-wide access
    accessible_resources = [
        "All Domain Controllers",
        "All File Servers",
        "All Database Servers",
        "All User Workstations",
        "Azure AD Connect Server",
        "Backup Systems"
    ]
    
    return jsonify({
        "krbtgt_compromised": True,
        "krbtgt_hash": f"{krbtgt_hash[:32]}...{krbtgt_hash[-16:]}",
        "golden_ticket_created": True,
        "fake_account": fake_admin,
        "ticket_lifetime_hours": ticket_lifetime,
        "domain_admin_access": True,
        "accessible_resources": accessible_resources,
        "persistence_achieved": True,
        "detection_triggered": True,
        "severity": "CRITICAL"
    })

@app.route('/api/logs')
def get_logs():
    """Get recent attack logs"""
    return jsonify({
        "attack_logs": attack_logs[-20:],
        "detection_events": detection_events[-20:]
    })

@app.route('/api/stats')
def get_stats():
    """Get attack statistics"""
    total_attacks = len(attack_logs)
    detected_attacks = len(detection_events)
    
    attack_types = {}
    for log in attack_logs:
        attack_type = log["attack_type"]
        attack_types[attack_type] = attack_types.get(attack_type, 0) + 1
    
    return jsonify({
        "total_attacks": total_attacks,
        "detected_attacks": detected_attacks,
        "detection_rate": round((detected_attacks / total_attacks * 100) if total_attacks > 0 else 0, 2),
        "attack_types": attack_types,
        "critical_events": len([e for e in detection_events if e["severity"] == "CRITICAL"])
    })

@app.route('/api/clear-logs', methods=['POST'])
def clear_logs():
    """Clear all logs"""
    global attack_logs, detection_events
    attack_logs = []
    detection_events = []
    return jsonify({"success": True, "message": "Logs cleared successfully"})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)