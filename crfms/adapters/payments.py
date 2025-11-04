import uuid
from ..domain.ports import Payment
from ..domain.users import Customer
from ..domain.values import Money

class FakePaymentError(Exception):
    """A custom exception to simulate a failed payment."""
    pass

class FakePaymentAdapter(Payment):
    """ A fake implementation of the Payment port. """
    
    def __init__(self):
        self.should_succeed = True

    def authorize_deposit(self, customer: Customer, amount: Money) -> str:
        """ Implements the 'authorize_deposit' method. """
        print(f"--- PAYMENT (DEPOSIT) ---")
        print(f"Authorizing ${amount.value:.2f} for {customer.email}...")
        
        if self.should_succeed:
            tx_id = f"fake_auth_{uuid.uuid4().hex[:10]}"
            print(f"Success! TX ID: {tx_id}")
            return tx_id
        else:
            print(f"Failure! (Simulated)")
            raise FakePaymentError("Simulated payment authorization failure")

    def finalize_payment(self, customer: Customer, amount: Money) -> str:
        """ Implements the 'finalize_payment' method."""
        print(f"--- PAYMENT (FINALIZE) ---")
        print(f"Charging ${amount.value:.2f} to {customer.email}...")
        
        if self.should_succeed:
            tx_id = f"fake_charge_{uuid.uuid4().hex[:10]}"
            print(f"Success! TX ID: {tx_id}")
            return tx_id
        else:
            print(f"Failure! (Simulated)")
            raise FakePaymentError("Simulated payment finalization failure")