import frappe
from frappe import _
from frappe.utils import get_url

def get_payment_url(**kwargs):
    """
    This function will be called by ERPNext webshop
    Returns the payment URL for CCAvenue
    """
    try:
        order_id = kwargs.get("order_id")
        if not order_id:
            frappe.logger().error("Order ID is missing in get_payment_url.")
            frappe.throw(_("Order ID is required"))

        # Debugging: Log the order ID
        frappe.logger().info(f"Generating payment URL for Order ID: {order_id}")

        payment_url = f"{get_url()}/api/method/custom_app.api.payment.initiate_ccavenue_payment?order_id={order_id}"

        # Debugging: Log the generated payment URL
        frappe.logger().info(f"Payment URL generated: {payment_url}")

        return payment_url
    except Exception as e:
        frappe.logger().error(f"Error in get_payment_url: {str(e)}")
        return None

def is_payment_gateway_enabled():
    """Check if CCAvenue payment gateway is enabled"""
    # Debugging: Log the gateway status
    frappe.logger().info("Checking if CCAvenue payment gateway is enabled.")
    return True

def validate_transaction_currency(currency):
    """
    Validate if the currency is supported by CCAvenue.
    """
    supported_currencies = ["INR", "USD", "EUR"]  # Update with your actual supported currencies

    # Debugging: Log the currency being validated
    frappe.logger().info(f"Validating currency: {currency}")

    if currency not in supported_currencies:
        frappe.logger().error(f"Unsupported currency: {currency}")
        frappe.throw(_("CCAvenue does not support transactions in the currency: {0}").format(currency))

    # Debugging: Log successful validation
    frappe.logger().info(f"Currency {currency} is supported.")
