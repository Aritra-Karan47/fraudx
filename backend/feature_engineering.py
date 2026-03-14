import numpy as np


def compute_features(wallet, transactions):

    sent = [tx for tx in transactions if tx["from"].lower() == wallet.lower()]
    received = [tx for tx in transactions if tx["to"].lower() == wallet.lower()]

    sent_values = [float(tx["value"]) for tx in sent]
    recv_values = [float(tx["value"]) for tx in received]

    sent_tx = len(sent)
    received_tx = len(received)

    total_tx = len(transactions)

    total_eth_sent = sum(sent_values)
    total_eth_received = sum(recv_values)

    unique_sent_addr = len(set(tx["to"] for tx in sent))
    unique_recv_addr = len(set(tx["from"] for tx in received))

    max_val_sent = max(sent_values) if sent_values else 0
    max_val_recv = max(recv_values) if recv_values else 0

    avg_val_sent = np.mean(sent_values) if sent_values else 0
    avg_val_recv = np.mean(recv_values) if recv_values else 0

    eth_balance = total_eth_received - total_eth_sent

    sent_received_ratio = sent_tx / (received_tx + 1)

    avg_tx_value = (total_eth_sent + total_eth_received) / (total_tx + 1)

    ether_flow = total_eth_received - total_eth_sent

    balance_ratio = eth_balance / (total_eth_received + 1)

    return {
        "sent_tx": sent_tx,
        "received_tx": received_tx,
        "unique_recv_addr": unique_recv_addr,
        "unique_sent_addr": unique_sent_addr,
        "max value received": max_val_recv,
        "avg val received": avg_val_recv,
        "max val sent": max_val_sent,
        "avg val sent": avg_val_sent,
        "total_tx": total_tx,
        "total_eth_sent": total_eth_sent,
        "total_eth_received": total_eth_received,
        "eth_balance": eth_balance,
        "sent_received_ratio": sent_received_ratio,
        "avg_tx_value": avg_tx_value,
        "ether_flow": ether_flow,
        "balance_ratio": balance_ratio,
    }
