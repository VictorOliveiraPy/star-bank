import starkbank

from src.domain.entities.invoice import Invoice


class InvoiceService:
    @classmethod
    def create_invoice(cls, create_invoice: Invoice):
        invoices = starkbank.invoice.create(create_invoice)
        return invoices
