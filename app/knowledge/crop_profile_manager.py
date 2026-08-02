"""
==========================================================================
AgriMind

Crop Profile Manager

Central manager for dynamic crop knowledge.

Workflow

Crop
   ↓
Repository
   ↓
Exists?
   ↓
YES → Load
NO  → Build → Validate → Save
   ↓
Return Profile

Author : AgriMind Team
==========================================================================
"""

import logging

from app.knowledge.crop_profile_builder import crop_profile_builder
from app.knowledge.crop_profile_validator import crop_profile_validator
from app.knowledge.crop_profile_repository import crop_profile_repository

logger = logging.getLogger(__name__)


class CropProfileManager:

    """
    Central crop knowledge manager.
    """

    ####################################################################
    # Load Existing or Build New
    ####################################################################

    def get_profile(

        self,

        crop

    ):

        crop = crop.lower().strip()

        ############################################################

        if crop_profile_repository.exists(crop):

            logger.info(

                f"Loaded crop profile for '{crop}' from database."

            )

            return crop_profile_repository.load(crop)

        ############################################################

        logger.info(

            f"Generating new crop profile for '{crop}'."

        )

        profile = crop_profile_builder.build(crop)

        crop_profile_validator.validate(profile)

        crop_profile_repository.save(profile)

        logger.info(

            f"Stored crop profile for '{crop}'."

        )

        return profile

    ####################################################################
    # Force Refresh
    ####################################################################

    def refresh_profile(

        self,

        crop

    ):

        crop = crop.lower().strip()

        logger.info(

            f"Refreshing profile for '{crop}'."

        )

        profile = crop_profile_builder.build(crop)

        crop_profile_validator.validate(profile)

        crop_profile_repository.update(profile)

        return profile

    ####################################################################
    # Delete
    ####################################################################

    def delete_profile(

        self,

        crop

    ):

        crop_profile_repository.delete(crop)

    ####################################################################
    # Available Crops
    ####################################################################

    def list_profiles(self):

        return crop_profile_repository.list_crops()


##########################################################################

crop_profile_manager = CropProfileManager()