# Save this to AutoLaunch

#!/usr/bin/env python3.7
import iterm2
# This script was created with the "basic" environment which does not support adding dependencies
# with pip.

async def main(connection):
    # Your code goes here. Here's a bit of example code that adds a tab to the current window:
    app = await iterm2.async_get_app(connection)
    @iterm2.RPC
    # Create action with: open_project(path:path, item:"Laravel")
    async def open_project(path, item):
        window = app.current_terminal_window
        await iterm2.Alert("", path + item).async_run(connection)
        if window is None:
            return

        if (item == "Laravel"):
            # Open VS Code for Laravel project
            session = app.current_terminal_window.current_tab.current_session
            await session.async_send_text('cd '+path+'\n')
            await session.async_send_text('code .\n')

            # Start laravel for Laravel project
            await window.async_create_tab()
            session = app.current_terminal_window.current_tab.current_session
            await session.async_send_text('cd '+path+'\n')
            await session.async_send_text('php artisan serve\n')

            # Start laravel-vite for Laravel project
            await window.async_create_tab()
            session = app.current_terminal_window.current_tab.current_session
            await session.async_send_text('cd '+path+'\n')
            await session.async_send_text('npm run dev\n') 



    await open_project.async_register(connection)


iterm2.run_forever(main)
