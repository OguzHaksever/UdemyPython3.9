def banner_text(user_input, screen_width=80):
    if len(user_input) > screen_width - 4:
        raise ValueError("\nString {0} is larger then specified width {1}"
                         .format(user_input, screen_width))

    if user_input == "*":
        print("*" * screen_width)
    else:
        output_string = "**{}**".format(user_input.center(screen_width - 4))
        print(output_string)


banner_text("*")
banner_text("What is love")
banner_text(" ")
banner_text("Baby don't hurt me")
banner_text("Don't hurt me")
banner_text(" ")
banner_text("No more")
banner_text("*")
banner_text(
    "this is too fucking long for anyone to care about in an easy coding lecture given by an aussie ")


(
    (
        (
            (
                (

                )

            )
        )
    )
)
