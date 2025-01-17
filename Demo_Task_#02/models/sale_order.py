from odoo import models, api, fields

# Demo Task : In the sale.order model, whenever the user edits the analytic distribution field, 
# then it must be changed in the invoice either if the invoice is generated or not.
class SaleOrder(models.Model):
    _inherit = 'sale.order'

    #Overiding the default write method which trigger when user edits any field in the record in the selected model  
    def write(self, vals):
        res = super(SaleOrder, self).write(vals)
        
        # (order_line), this field connects sale.order with sale.order.line
        if 'order_line' in vals: 
            
            for order in self:
                
                for line in order.order_line:
                
                    if line.analytic_distribution:  

                        # (invoice_ids), this field connects sale.order with account.move
                        # filtered(lambda inv: inv.state != 'cancel') can also apply this attribute with the 
                        # above line to just get the invoices whose state are not cancelled
                        invoices = order.invoice_ids 
                        
                        # accessing a single invoice from invoices because there may be multiple invoices
                        for invoice in invoices:

                            # (invoice_line_ids), this field connects sale.order with account.move                          
                            for invoice_line in invoice.invoice_line_ids:
                                
                                # accessing the same product from quotation to invoice through product_id
                                if invoice_line.product_id == line.product_id:
                                
                                    # Writing the value of analytic distribution to the invoice products respecctively
                                    invoice_line.write({'analytic_distribution': line.analytic_distribution})
                                    
        return res

    

                    
