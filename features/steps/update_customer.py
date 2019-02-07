from behave import when


@when(u'I change my surname to "{new_surname}"')
def update_surname(context, new_surname):
    context.response =\
        context.web_client.post(f'/customers/update/{context.customer_id}',
                                json={'newSurname': new_surname})
