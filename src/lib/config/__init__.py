general_rules = {
    "datasets.{*}.size": {'type': int, 'none': False},
    "datasets.{*}.locale": {'type': str, 'none': False},
    "datasets.{*}.fields.[*].type": {'type': str, 'none': False},
    "datasets.{*}.fields.[*].name": {'type': str, 'none': False},
    "datasets.{*}.fields.[*].generator": {'type': dict, 'none': False},
    "datasets.{*}.format.type": {'type': str, 'none': False},
    "datasets.{*}.serializers.to.[*].type": {'type': str, 'none': False}
}
