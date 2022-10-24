<template>
<body >
    <headerComponent></headerComponent>
    
    <main  class = "text-center">
        <section class=" text-center">
			<div class="container">
				<h1 class = "p-3">Login</h1>
			</div>
		</section>

        <b-form class="form-signin">
            <div class = "p-3 pb-5">
                <img class="mb-4" src="@/assets/img/smile.png" alt="" width="72" height="72">
                <div>
                    <label for="inputEmail" class="sr-only">Email address</label>
                    <input type="email" id="inputEmail" class="form-control" placeholder="Email address" required autofocus>
                </div>
                <div>
                    <label for="inputPassword" class="sr-only">Password</label>
                    <input type="password" id="inputPassword" class="form-control" placeholder="Password" required>
                </div>
                <!-- <div class="checkbox mb-3">
                    <label>
                    <input type="checkbox" value="remember-me"> Remember me
                    </label>
                </div> -->
                <button class="btn btn-lg btn-dark btn-block" type="submit">Sign in</button>
                <div class = "pt-2">
                    <a class=" text-muted" href = "#/register">register</a>
                </div>
                <!-- <p class="mt-5 mb-3 text-muted">&copy; 2017-2022</p> -->
            </div>
        </b-form>

    </main>
</body>
</template>

<script>
    
    export default{
        name:"indexPage",
        components:{
            'headerComponent':()=> import('@/components/basic/headerComponent.vue')
        },
    }
</script>


