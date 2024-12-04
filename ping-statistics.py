# -*- coding: utf-8 -*-
"""
Created on Tue Dec  3 05:54:47 2024

@author: IAN CARTER KULANI
"""

import matplotlib.pyplot as plt
from ping3 import ping, verbose_ping

def ping_server(server, count=4):
    success_count = 0
    fail_count = 0

    for _ in range(count):
        response = ping(server)
        if response is not None:
            success_count += 1
        else:
            fail_count += 1

    return success_count, fail_count

def visualize_results(success, fail):
    labels = 'Success', 'Fail'
    sizes = [success, fail]
    colors = ['#4CAF50', '#F44336']  # Green for success, Red for fail
    explode = (0.1, 0)  # explode the success slice

    plt.figure(figsize=(6, 6))
    plt.pie(sizes, explode=explode, labels=labels, colors=colors,
            autopct='%1.1f%%', shadow=True, startangle=140)
    plt.axis('equal')  # Equal aspect ratio ensures the pie chart is circular.
    plt.title('Ping Results')
    plt.show()

def main():
    server = input("Enter the server IP or hostname to ping: ")
    count = int(input("Enter the number of pings to perform: "))
   
    success, fail = ping_server(server, count)
    print(f"Success: {success}, Fail: {fail}")
    visualize_results(success, fail)

if __name__ == "__main__":
    main()