import asyncio
import os

PYPPETEER_CHROMIUM_REVISION = '1263111'

os.environ['PYPPETEER_CHROMIUM_REVISION'] = PYPPETEER_CHROMIUM_REVISION
from pyppeteer import launch

async def generate_pdf(url, pdf_path):
    browser = await launch()
    page = await browser.newPage()
    
    await page.goto(url)
    
    await page.pdf({'path': pdf_path, 'format': 'A3'})
    
    await browser.close()

# Run the function
asyncio.get_event_loop().run_until_complete(generate_pdf('file:///C:/Users/bernardo.castillo/Documents/Projetos%20CDV/Relatorio.html', 'RelatorioPDF.pdf'))