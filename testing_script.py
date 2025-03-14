import aiohttp
import httpx
import requests
import asyncio
import time

URL = "http://192.168.138.132:8000/abantu/"

def fetch_requests():
    start = time.time()
    response = requests.get(URL)
    elapsed = time.time() - start

    print("\n[Synchronous - requests]")
    print("Status:", response.status_code)
    print("Content-type:", response.headers.get("content-type", "N/A"))
    print("Body:", response.text[:15], "...")
    print(f"Time taken: {elapsed:.4f} seconds")

async def fetch_aiohttp():
    start = time.time()
    async with aiohttp.ClientSession() as session:
        async with session.get(URL) as response:
            html = await response.text()
            elapsed = time.time() - start

            print("\n[Asynchronous - aiohttp]")
            print("Status:", response.status)
            print("Content-type:", response.headers.get("content-type", "N/A"))
            print("Body:", html[:15], "...")
            print(f"Time taken: {elapsed:.4f} seconds")

async def fetch_httpx():
    start = time.time()
    async with httpx.AsyncClient() as client:
        response = await client.get(URL)
        elapsed = time.time() - start

        print("\n[Asynchronous - httpx]")
        print("Status:", response.status_code)
        print("Content-type:", response.headers.get("content-type", "N/A"))
        print("Body:", response.text[:15], "...")
        print(f"Time taken: {elapsed:.4f} seconds")

async def main():
    fetch_requests()
    await asyncio.gather(fetch_aiohttp(), fetch_httpx())

asyncio.run(main())
