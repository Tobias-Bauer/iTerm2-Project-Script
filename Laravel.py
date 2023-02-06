async def Laravel(app, dir):
    window = app.current_terminal_window

    # Open VS Code for Laravel project
    session = app.current_terminal_window.current_tab.current_session
    await session.async_send_text('cd '+dir+'\n')
    await session.async_send_text('code .\n')

    # Start laravel for Laravel project
    await window.async_create_tab()
    session = app.current_terminal_window.current_tab.current_session
    await session.async_send_text('cd '+dir+'\n')
    await session.async_send_text('php artisan serve\n')

    # Start laravel-vite for Laravel project
    await window.async_create_tab()
    session = app.current_terminal_window.current_tab.current_session
    await session.async_send_text('cd '+dir+'\n')
    await session.async_send_text('npm run dev\n') 
