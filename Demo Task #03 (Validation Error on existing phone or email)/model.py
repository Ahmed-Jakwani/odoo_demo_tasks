# Demo Task 03: In the customers view, when creating a new contact, 
# if the user enters mobile number or email which is already associated with an existing customer, 
# then it will show a validation error.                            
class ResPartner(models.Model):
    _inherit = 'res.partner'

    #This method will invoke whenever a new record is created.
    @api.model
    def create(self, values):
        
        error =[]
        
        #Checking for the phone field
        if 'phone' in values and values['phone']:
            
            #Searching as if the phone value is associated with any other record, 
            # if associated with multiple record then get the first match
            validate_phone = self.search([('phone', '=', values['phone'])], limit = 1)
            
            #If associated then generated then add error message in the errors[]
            if validate_phone:
                error.append(f"The phone number {values['phone']} is already associated with {validate_phone.name}.")
       
        #Checking for the email field
        if 'email' in values and values['email']:
            
            #Searching as if the email value is associated with any other record,
            # if associated with multiple record then get the first match
            validate_email = self.search([('email', '=', values['email'])], limit = 1)
            
            #If associated then generated then add error message in the errors[]
            if validate_email:
                error.append(f"The email {values['email']} is already associated with {validate_email.name}.")
               
        #if there are error messages in the list, show them on validation error 
        if error:
            raise ValidationError("\n".join(error))


        return super(ResPartner, self).create(values)