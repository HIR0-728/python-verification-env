import asyncio
import os


async def async_run_command(cmd: str) -> None:
    proc = await asyncio.create_subprocess_shell(
        cmd,
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE,
    )

    _, stderr = await proc.communicate()

    if stderr:
        print(stderr.decode())
        raise Exception(stderr.decode())


async def main():
    try:
        input_dir = "./input"
        output_dir = "./output"

        files = os.listdir(input_dir)

        for file in files:
            print(f"Processing file: {file}")

            convert_input_file = os.path.join(input_dir, file)
            # ファイル名と拡張子を分離
            file_name, file_ext = os.path.splitext(file)
            # output_file_pathを更新
            output_file_path = os.path.join(output_dir, f"{file_name}_{file_ext[1:]}")

            cmd = (
                "libreoffice --nolockcheck --nologo --headless --norestore "
                "--language=ja --nofirststartwizard --convert-to pdf:writer_pdf_Export --outdir "
                f"{output_file_path} {convert_input_file}"
            )
            await async_run_command(cmd)

    except Exception as e:
        print(e)
    finally:
        print("Done")


if __name__ == "__main__":

    asyncio.run(main())
