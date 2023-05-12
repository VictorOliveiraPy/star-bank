import logging

from src.domain.entities.invoice import Invoice
from src.services.invoice.invoice_service import InvoiceService


class CreateInvoiceUseCase:
    @classmethod
    def generate_random_invoices(cls, create_invoice: Invoice):
        try:
            logging.info(
                f"[Create-Invoice] - Starting Invoice Of The Invoice {create_invoice.name}"
            )
            service = InvoiceService.create_invoice(create_invoice)
            logging.info(
                f"[Create-Invoice] - Invoice Created Successfully for {create_invoice.name}"
            )
            return service
        except Exception as e:
            logging.error(
                f"[Create-Invoice] - Failed to create invoice for {create_invoice.name}. Error: {str(e)}"
            )
