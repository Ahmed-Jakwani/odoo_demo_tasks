from odoo import models, api, fields

#Demo Task 01: In the quotation view of sale module, whenever the user edits the analytic distribution field, 
# then it must be changed in the invoice either if the invoice is generated or not.
class SaleOrder(models.Model):
    _inherit = 'sale.order'

    #Overiding the default write method which trigger when user edits any field in the record in the selected model  
    def write(self, vals):
        res = super(SaleOrder, self).write(vals)
        
        # (order_line), the field connects sale.order with sale.order.line
        if 'order_line' in vals: 
            
            for order in self:
                
                for line in order.order_line:

                    #If the analytic_distribution is updated then line is having 
                    # a key of that and it will be called as an attribute                   
                    if line.analytic_distribution:  

                        # this will bring the invoices associated with quotation which is just updated 
                        # because the invoice_ids is one2many field connect with account.move model
                        # filtered(lambda inv: inv.state != 'cancel') can also apply this attribute with the 
                        # above line to just get the invoices whose state are not cancelled
                        invoices = order.invoice_ids 
                        
                        # accessing a single invoice from invoices because there may be multiple invoices
                        # and through this can also access attributes like invoice.product_id.name
                        for invoice in invoices:

                            # accessing the fields of account.move.line model through the invoice_line_ids
                            # and can write in the account.move.line fields                            
                            for invoice_line in invoice.invoice_line_ids:
                                
                                # accessing the same product from quotation to invoice through product_id
                                if invoice_line.product_id == line.product_id:
                                
                                    # Writing the value of analytic distribution to the invoice products respecctively
                                    invoice_line.write({'analytic_distribution': line.analytic_distribution})
                                    
        return res


                    
