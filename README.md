# SauceDemo Playwright E2E Demo

A small, public QA automation portfolio project built with **Python + pytest + Playwright**.

The goal is to demonstrate a maintainable E2E structure without exposing any code, test data, or business logic from previous employers.

## Architecture

```text
saucedemo-playwright-demo/
├── components/
│   └── header_component.py
├── pages/
│   ├── base_page.py
│   ├── login_page.py
│   ├── inventory_page.py
│   ├── cart_page.py
│   └── checkout_page.py
├── tests/
│   ├── test_login.py
│   ├── test_cart.py
│   └── test_checkout.py
├── conftest.py
├── pytest.ini
└── requirements.txt
```

### Design idea

- **BasePage**: shared navigation / common page behavior
- **Page Classes**: page-specific locators and actions
- **Component Classes**: reusable UI parts shared across pages
- **pytest fixtures**: browser/page setup and reusable login state
- **Tests**: readable business scenarios with minimal locator details

## Covered scenarios

1. Successful login
2. Invalid login
3. Add product to cart
4. Remove product from cart
5. Complete checkout successfully

## Setup

```bash
python -m venv .venv
```

Windows:

```bash
.venv\Scripts\activate
```

macOS / Linux:

```bash
source .venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
playwright install
```

Run tests:

```bash
pytest
```

Run with visible browser:

```bash
pytest --headed
```

## Demo target

This project uses the public SauceDemo test site:

`https://www.saucedemo.com`

No production credentials, customer data, or employer-owned source code are included.
