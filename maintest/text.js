<!-- application code -->
<script type="text/javascript">
  userbase.init({ appId: 'YOUR_APP_ID' })

  function handleSignUp(e) {
    e.preventDefault()

    const username = document.getElementById('signup-username').value
    const password = document.getElementById('signup-password').value

    userbase.signUp({ username, password, rememberMe: 'none' })
      .then((user) => alert('You signed up!'))
      .catch((e) => document.getElementById('signup-error').innerHTML = e)
  }

  document.getElementById('signup-form').addEventListener('submit', handleSignUp)
</script>