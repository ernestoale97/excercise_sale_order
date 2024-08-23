# Sales Order Expiration Date Feature

## Overview

This module extends the Odoo Sales module by adding an expiration date feature to sales orders. The feature ensures that orders are confirmed or rejected within a specified time frame, improving order management and reducing the risk of outdated or forgotten orders.

## Features

1. **Expiration Date Field:**
   - Adds a new field to the Sales Order form to specify an expiration date.
   - The expiration date can be manually set by the sales representative or automatically calculated based on a predefined rule (e.g., 7 days from the order date).

2. **Expiration Warning:**
   - Implements a warning notification that appears when a sales order is approaching its expiration date (e.g., within 2 days).
   - The notification is visible to the responsible sales representative and appears on the Sales Order dashboard.

3. **Automatic Cancellation:**
   - Adds an option to automatically cancel sales orders that have passed their expiration date without being confirmed.
   - This feature is configurable, allowing users to enable or disable automatic cancellations.

4. **Filter and Reporting:**
   - Adds filters in the Sales Order list view to quickly identify orders that are about to expire or have already expired.
   - Provides a simple report showing the number of expired orders over a given period, along with potential revenue loss from unconfirmed orders.

5. **User Roles and Access Control:**
   - Ensures that only authorized users (e.g., sales managers) can change the expiration date or override automatic cancellation settings.

## Installation

1. Copy the module into your Odoo `addons` directory.
2. Update the Odoo app list and install the module.
3. Configure the expiration date settings under Sales settings.

## Usage

- **Setting Expiration Date:** When creating a sales order, set the expiration date manually, or allow it to be automatically calculated.
- **Receiving Expiration Warnings:** Sales representatives will see a warning notification for orders approaching their expiration date.
- **Automatic Cancellation:** If enabled, orders that pass their expiration date without confirmation will be automatically canceled.
- **Monitoring Expiration:** Use the provided filters and reports to monitor expiring or expired orders.

## Configuration

- Go to **Sales > Configuration > Settings** to set up default expiration rules and enable or disable automatic cancellation.

## Security

- Access control ensures that only authorized users can modify expiration dates and settings.

## Compatibility

- Compatible with Odoo 15.0.
- Ensure that the expiration date logic does not interfere with any other customizations or workflows within the Sales module.

## License

This module is licensed under the [MIT License](LICENSE).