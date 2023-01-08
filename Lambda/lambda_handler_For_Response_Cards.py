import json

burger_sizes = ['single', 'double', 'triple']
burger_franchises = ['best burger', 'burger palace', 'flaming burger']
best_burger_types = ['plain', 'cheese', 'bacon']
burger_palace_types = ['fried egg', 'fried pickle', 'fried green tomatoes']
flaming_burger_types = ['chili', 'jalapeno', 'peppercorn']


def validate_order(slots):
    # Validate BurgerSize
    if not slots['BurgerSize']:
        print('Validating BurgerSize Slot')

        return {
            'isValid': False,
            'invalidSlot': 'BurgerSize'
        }

    if slots['BurgerSize']['value']['originalValue'].lower() not in burger_sizes:
        print('Invalid BurgerSize')

        return {
            'isValid': False,
            'invalidSlot': 'BurgerSize',
            'message': 'Please select a {} burger size.'.format(", ".join(burger_sizes))
        }

    # Validate BurgerFranchise
    if not slots['BurgerFranchise']:
        print('Validating BurgerFranchise Slot')

        return {
            'isValid': False,
            'invalidSlot': 'BurgerFranchise'
        }

    if slots['BurgerFranchise']['value']['originalValue'].lower() not in burger_franchises:
        print('Invalid BurgerSize')

        return {
            'isValid': False,
            'invalidSlot': 'BurgerFranchise',
            'message': 'Please select from {} burger franchises.'.format(", ".join(burger_franchises))
        }

    # Validate BurgerType
    if not slots['BurgerType']:
        print('Validating BurgerType Slot')

        return {
            'isValid': False,
            'invalidSlot': 'BurgerType',
            'invalidFranchise': ''
        }

    # Validate BurgerType for BurgerFranchise
    if slots['BurgerFranchise']['value']['originalValue'].lower() == 'best burger':
        if slots['BurgerType']['value']['originalValue'].lower() not in best_burger_types:
            print('Invalid BurgerType for Best Burger')

            return {
                'isValid': False,
                'invalidSlot': 'BurgerType',
                'invalidFranchise': 'best_burger',
                'message': 'Please select a Best Burger type of {}.'.format(", ".join(best_burger_types))
            }

    if slots['BurgerFranchise']['value']['originalValue'].lower() == 'burger palace':
        if slots['BurgerType']['value']['originalValue'].lower() not in burger_palace_types:
            print('Invalid BurgerType for Burger Palace')

            return {
                'isValid': False,
                'invalidSlot': 'BurgerType',
                'invalidFranchise': 'burger_palace',
                'message': 'Please select a Burger Palce type of {}.'.format(", ".join(burger_palace_types))
            }

    if slots['BurgerFranchise']['value']['originalValue'].lower() == 'flaming burger':
        if slots['BurgerType']['value']['originalValue'].lower() not in flaming_burger_types:
            print('Invalid BurgerType for Flaming Burger')

            return {
                'isValid': False,
                'invalidSlot': 'BurgerType',
                'invalidFranchise': 'flaming_burger',
                'message': 'Please select a Flaming Burger type of {}.'.format(", ".join(flaming_burger_types))
            }

    # Valid Order
    return {'isValid': True}


def lambda_handler(event, context):
    print(event)

    bot = event['bot']['name']
    slots = event['sessionState']['intent']['slots']
    intent = event['sessionState']['intent']['name']

    order_validation_result = validate_order(slots)
    print(order_validation_result)

    if event['invocationSource'] == 'DialogCodeHook':
        if not order_validation_result['isValid']:
            response_message = 'BurgerBuddy'
            if 'message' in order_validation_result:
                response_message = order_validation_result['message']

            response_card_sub_title = ''
            response_card_buttons = []

            best_burger_sub_title = 'Please select a Best Burger type'
            best_burger_buttons = [
                {
                    "text": "Plain",
                    "value": "plain"
                },
                {
                    "text": "Cheese",
                    "value": "cheese"
                },
                {
                    "text": "Bacon",
                    "value": "bacon"
                }
            ]

            burger_palace_sub_title = 'Please select a Burger Palace type'
            burger_palace_buttons = [
                {
                    "text": "Fried Egg",
                    "value": "fried egg"
                },
                {
                    "text": "Fried Pickle",
                    "value": "fried pickle"
                },
                {
                    "text": "Fried Green Tomatoes",
                    "value": "fried green tomatoes"
                }
            ]

            flaming_burger_sub_title = 'Please select a Flaming Burger type'
            flaming_burger_buttons = [
                {
                    "text": "Chili",
                    "value": "chili"
                },
                {
                    "text": "Jalapeno",
                    "value": "jalapeno"
                },
                {
                    "text": "peppercorn",
                    "value": "Peppercorn"
                }
            ]

            if order_validation_result['invalidSlot'] == "BurgerSize":
                response_card_sub_title = "Please select a Burger size"
                response_card_buttons = [
                    {
                        "text": "Single",
                        "value": "single"
                    },
                    {
                        "text": "Double",
                        "value": "double"
                    },
                    {
                        "text": "Triple",
                        "value": "triple"
                    }
                ]

            if order_validation_result['invalidSlot'] == "BurgerFranchise":
                response_card_sub_title = "Please select a Burger Franchise"
                response_card_buttons = [
                    {
                        "text": "Best Burger",
                        "value": "best burger"
                    },
                    {
                        "text": "Burger Palace",
                        "value": "burger palace"
                    },
                    {
                        "text": "Flaming Burger",
                        "value": "flaming burger"
                    }
                ]

            if order_validation_result['invalidSlot'] == "BurgerType":
                if order_validation_result['invalidFranchise'] == "best_burger":
                    response_card_sub_title = best_burger_sub_title
                    response_card_buttons = best_burger_buttons
                elif order_validation_result['invalidFranchise'] == "burger_palace":
                    response_card_sub_title = burger_palace_sub_title
                    response_card_buttons: burger_palace_buttons
                elif order_validation_result['invalidFranchise'] == "flaming_burger":
                    response_card_sub_title = flaming_burger_sub_title
                    response_card_buttons: flaming_burger_buttons
                else:
                    response_card_sub_title = 'Please select a burger type'
                    response_card_buttons = [
                        {
                            "text": "Plain",
                            "value": "plain"
                        },
                        {
                            "text": "Cheese",
                            "value": "cheese"
                        },
                        {
                            "text": "Bacon",
                            "value": "bacon"
                        }
                        ,
                        {
                            "text": "Fried Pickle",
                            "value": "fried pickle"
                        },
                        {
                            "text": "Chili",
                            "value": "chili"
                        }
                    ]

            response = {
                "sessionState": {
                    "dialogAction": {
                        "slotToElicit": order_validation_result['invalidSlot'],
                        "type": "ElicitSlot"
                    },
                    "intent": {
                        "name": intent,
                        "slots": slots,
                    }
                },
                "messages": [
                    {
                        "contentType": "ImageResponseCard",
                        "content": response_message,
                        "imageResponseCard": {
                            "title": "BurgerBuddy",
                            "subtitle": response_card_sub_title,
                            "imageUrl": "YOUR_IMAGE_URL_HERE",
                            "buttons": response_card_buttons
                        }
                    }
                ]
            }
        else:
            response = {
                "sessionState": {
                    "dialogAction": {
                        "type": "Delegate"
                    },
                    "intent": {
                        'name': intent,
                        'slots': slots
                    }
                }
            }

    if event['invocationSource'] == 'FulfillmentCodeHook':
        response = {
            "sessionState": {
                "dialogAction": {
                    "type": "Close"
                },
                "intent": {
                    "name": intent,
                    "slots": slots,
                    "state": "Fulfilled"
                }
            },
            "messages": [
                {
                    "contentType": "PlainText",
                    "content": "I've placed your order."
                }
            ]
        }

    print(response)
    return response
