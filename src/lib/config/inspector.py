from re import match


class ConfigurationInpector(object):
    def __validate_none(self, value, expected):
        return expected.get('none') is False and value is None

    def __validate_type(self, value, expected):
        return not isinstance(value, expected['type'])

    def __validate(self,
                   configuration: dict,
                   rule: str,
                   expected: dict,
                   optional: bool):
        keys = rule.split('.')
        key = keys[0]

        if self.__validate_none(value=configuration.get(key),
                                expected=expected) and \
           optional is False:
            raise ValueError(f"JSON Key `{key}` can not "
                             "be `None`, `null` or empty")
        elif optional is True:
            return

        if len(keys) > 1:
            return

        value = configuration.get(key)
        if self.__validate_type(value=value, expected=expected):
            expected_type = expected['type']
            if expected_type == dict:
                expected_type = type(expected_type)
            raise ValueError(f"JSON Key `{key}` must be "
                             f"of type `{expected_type}`")

        custom_rules = expected.get('custom', [])
        if len(custom_rules) > 0:
            for custom in custom_rules:
                custom(value)

    def inspect_rule(self,
                     configuration: dict,
                     rule: str,
                     expected: dict,
                     optional: bool = False):
        current_key = rule.split('.')[0]
        partial_rule = rule.replace(f'{current_key}.', "")

        if match(r'[{\[].*[}\]]', current_key):
            if current_key[1] == '*':  # Iterable
                if current_key[0] == '[':  # List
                    for item in configuration:
                        return self.inspect_rule(configuration=item,
                                                 expected=expected,
                                                 rule=partial_rule,
                                                 optional=optional)
                    raise ValueError(f"Key '{current_key}' has "
                                     "no valid values")
                else:  # Dict
                    for key in configuration.keys():
                        return self.inspect_rule(
                            configuration=configuration[key],
                            expected=expected,
                            rule=partial_rule,
                            optional=optional
                        )
            else:  # Fixed Index
                index = current_key[1:-1]
                if current_key[0] == '[':  # List
                    index = int(index)
                    return self.inspect_rule(
                        configuration=configuration[index],
                        expected=expected,
                        rule=partial_rule,
                        optional=optional
                    )
                else:  # Dict
                    return self.inspect_rule(
                        configuration=configuration[index],
                        expected=expected,
                        rule=partial_rule,
                        optional=optional
                    )

        self.__validate(configuration=configuration,
                        rule=rule,
                        expected=expected,
                        optional=optional)
        if '.' not in rule or \
           (current_key not in configuration and optional is True):
            return
        return self.inspect_rule(configuration=configuration[current_key],
                                 expected=expected,
                                 rule=partial_rule,
                                 optional=optional)

    def inspect_rules(self, rules, configuration, optional=False):
        for rule_key in rules.keys():
            self.inspect_rule(rule=rule_key,
                              expected=rules[rule_key],
                              configuration=configuration,
                              optional=optional)
