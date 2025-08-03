"""
check_unused_accounts.py

This script helps identify unused accounts from a list, simulating CIS Control #5 (Account Management).
In a real-world system, you'd pull this from an actual user database or OS user list.
"""

def identify_unused_accounts(account_activity, days_threshold=90):
    """
    Identify accounts not used in the past `days_threshold` days.

    Parameters:
        account_activity (dict): account name -> days since last activity
        days_threshold (int): threshold to flag unused accounts

    Returns:
        List of unused account names
    """
    return [user for user, days in account_activity.items() if days > days_threshold]

# Example usage
if __name__ == "__main__":
    sample_accounts = {
        "admin": 12,
        "temp_user": 194,
        "jane_hr": 3,
        "bob_sales": 105
    }

    unused = identify_unused_accounts(sample_accounts)
    print("Unused accounts:", unused)
