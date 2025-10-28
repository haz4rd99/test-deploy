app_name = "tideshift_minimal"
app_title = "Tideshift Minimal"
app_publisher = "Mike"
app_description = "Minimal Tideshift test app"
app_email = "mike@casualty.co.nz"
app_license = "mit"

# Required apps for cloud deployment
required_apps = ["frappe", "erpnext", "hrms"]

# Build Configuration
# -------------------
# Skip asset building - no frontend assets
skip_assets_build = True

# Installation
# ------------
after_install = "tideshift_minimal.install.after_install"

