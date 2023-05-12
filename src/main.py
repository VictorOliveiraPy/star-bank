import logging
from datetime import datetime

from apscheduler.schedulers.blocking import BlockingScheduler
from fastapi import FastAPI

from src.application.use_cases.invoice.create_invoice_use_case import \
    CreateInvoiceUseCase
from src.domain.entities.invoice import (Invoice, InvoiceDescription,
                                         InvoiceDiscount)

app = FastAPI()


@app.get("/ping")
async def pong():
    return {"Star": "Bank!"}


def wrapper_generate_random_invoices():
    invoices = [
        Invoice(
            amount=400000,
            descriptions=[InvoiceDescription(key="Arya", value="Not today")],
            discounts=[
                InvoiceDiscount(
                    percentage=10, due=datetime(2021, 3, 12, 15, 23, 26, 689377)
                )
            ],
            due=datetime(2021, 5, 12, 15, 23, 26, 689377),
            expiration=123456789,
            fine=2.5,
            interest=1.3,
            name="Arya Stark",
            tags=["War supply", "Invoice #1234"],
            tax_id="012.345.678-90",
        )
    ]
    CreateInvoiceUseCase.generate_random_invoices(invoices)


if __name__ == "__main__":
    scheduler = BlockingScheduler()
    logging.info(f"[BlockingScheduler] - Starting")
    print("oi")

    scheduler.add_job(
        wrapper_generate_random_invoices,
        "cron",
        # hour=settings.CRON_JOB_INTERVAL,
        second=1,
    )
    scheduler.start()
