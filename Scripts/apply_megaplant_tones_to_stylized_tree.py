import unreal


LEAF_ROOT = "/Game/Stylized_Tree_Pack/Materials/Material_Instances"

# Darker, more natural tones close to the MegaPlants Aleppo pine assets.
LEAF_COLOR_A = unreal.LinearColor(0.055, 0.085, 0.055, 1.0)
LEAF_COLOR_B = unreal.LinearColor(0.155, 0.185, 0.105, 1.0)
BRANCH_LEAF_A = unreal.LinearColor(0.045, 0.065, 0.040, 1.0)
BRANCH_LEAF_B = unreal.LinearColor(0.115, 0.135, 0.075, 1.0)
BARK_COLOR = unreal.LinearColor(0.145, 0.115, 0.085, 1.0)

LEAF_INTENSITY = 0.82
BRANCH_LEAF_INTENSITY = 0.70
GRADIENT_INTENSITY = 0.35


def is_material_instance(asset):
    return isinstance(asset, unreal.MaterialInstanceConstant)


def set_vector(instance, name, color):
    unreal.MaterialEditingLibrary.set_material_instance_vector_parameter_value(
        instance, name, color
    )


def set_scalar(instance, name, value):
    unreal.MaterialEditingLibrary.set_material_instance_scalar_parameter_value(
        instance, name, value
    )


def apply_leaf_tone(instance, asset_path):
    branch = "/Branch/" in asset_path or "_Branch_" in asset_path
    set_vector(instance, "Leaf Color A", BRANCH_LEAF_A if branch else LEAF_COLOR_A)
    set_vector(instance, "Leaf Color B", BRANCH_LEAF_B if branch else LEAF_COLOR_B)
    set_scalar(instance, "Leaf Color Intensity", BRANCH_LEAF_INTENSITY if branch else LEAF_INTENSITY)
    set_scalar(instance, "Gradient Intensity", GRADIENT_INTENSITY)


def apply_bark_tone(instance):
    set_vector(instance, "Opacity Color", BARK_COLOR)


def main():
    registry = unreal.AssetRegistryHelpers.get_asset_registry()
    assets = registry.get_assets_by_path(LEAF_ROOT, recursive=True)

    changed = []
    skipped = []

    for asset_data in assets:
        asset_name = str(asset_data.asset_name)
        package_name = str(asset_data.package_name)
        asset_path = "{}.{}".format(package_name, asset_name)

        if not (asset_name.startswith("MI_Leaf_") or asset_name.startswith("MI_Bark_")):
            continue

        asset = asset_data.get_asset()
        if not is_material_instance(asset):
            skipped.append(asset_path)
            continue

        if asset_name.startswith("MI_Leaf_"):
            apply_leaf_tone(asset, asset_path)
        else:
            apply_bark_tone(asset)

        unreal.EditorAssetLibrary.save_loaded_asset(asset)
        changed.append(asset_path)

    unreal.log("MegaPlants tone pass complete.")
    unreal.log("Changed material instances: {}".format(len(changed)))
    for path in changed:
        unreal.log("  changed: {}".format(path))
    if skipped:
        unreal.log_warning("Skipped non-material assets: {}".format(len(skipped)))


main()
