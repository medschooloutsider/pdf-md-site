# pdf.md Commerce Setup

Use this when creating the first sellable Lemon Squeezy configuration for `pdf.md`.

## Goal

- One product
- One one-time price
- License keys enabled
- Hosted checkout URL copied back into the app bundle as `PDFMDPurchaseURL`

## Lemon Squeezy Product

- Product name: `pdf.md`
- Product type: digital product / software
- Price: `$29`
- Billing model: one-time purchase
- Variant name: `Personal License`

## License Settings

Enable license keys for the product variant.

Recommended first settings:

- Generate License Keys: `On`
- License length: `Unlimited`
- Activation limit: `2`

This matches the current app-side assumption:

- one purchaser
- personal license
- up to 2 Macs

## Checkout

Use Lemon Squeezy hosted checkout, not a custom cart URL.

The shareable checkout URL should look like:

- `https://[STORE].lemonsqueezy.com/checkout/buy/[VARIANT_ID]`

Do not copy a converted cart URL that contains:

- `/checkout/?cart=`

Only the `/checkout/buy/` URL should be stored in the app.

## App Wiring

After the product is created, copy the hosted checkout URL into:

- `AppBundleTemplate/Contents/Info.plist`
- key: `PDFMDPurchaseURL`

Support is already wired via:

- key: `PDFMDSupportEmail`
- current value: `worldpresident1030@gmail.com`

The licensing API base is already wired via:

- key: `PDFMDLicenseAPIBaseURL`
- value: `https://api.lemonsqueezy.com`

## Customer Flow

1. Customer clicks `Buy License`
2. Lemon Squeezy hosted checkout opens
3. Customer completes purchase
4. Lemon Squeezy emails the receipt and license key
5. Customer opens `pdf.md`
6. Customer enters license key in License Manager
7. App activates the key through Lemon Squeezy License API

## Post-Setup Test

Run one real end-to-end test:

1. Open the hosted checkout URL
2. Complete a purchase
3. Confirm the license key is present in the receipt or My Orders
4. Activate inside `pdf.md`
5. Validate once
6. Deactivate once
7. Re-activate once

## Official References

- Lemon Squeezy license keys: `https://docs.lemonsqueezy.com/help/licensing/generating-license-keys`
- Lemon Squeezy License API: `https://docs.lemonsqueezy.com/api/license-api`
- Lemon Squeezy hosted checkout: `https://docs.lemonsqueezy.com/help/checkout/hosted-checkout`
- Lemon Squeezy product sharing: `https://docs.lemonsqueezy.com/help/products/sharing-products`
