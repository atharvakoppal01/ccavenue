import frappe
from frappe.model.document import Document

class CCavenueSettings(Document):
    def validate(self):
        if self.is_enabled:
            if not self.merchant_id or not self.access_code or not self.working_key:
                frappe.throw("Merchant ID, Access Code and Working Key are required")