import asyncio
import sys
APPLICATION_LIST = [
    {}
]
async def npm_build():
    process = await asyncio.create_subprocess_shell(
        'cd frontend && npm run build',
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE
    )
    stdout, stderr = await process.communicate()
    print(stdout.decode())
    print(stderr.decode())

async def main():
    await npm_build()

if __name__ == "__main__":
    print(asyncio.run(main()))