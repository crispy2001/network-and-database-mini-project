<template>
    <body class = "test-background">
        <headerComponent></headerComponent>
        
        <main  class = "text-center">
            <section class=" text-center">
                <div class="container">
                    <h1 class = "p-3">Login</h1>
                </div>
            </section>
    
            <form class="form-signin">
                <div class = "p-3 pb-5">
                    <img class="mb-4" src="@/assets/img/smile.png" alt="" width="72" height="72">
                    <label for="inputEmail" class="sr-only">Email address</label>
                    <input type="email" id="inputEmail" class="form-control" placeholder="Email address" required autofocus>
                    <label for="inputPassword" class="sr-only">Password</label>
                    <input type="password" id="inputPassword" class="form-control" placeholder="Password" required>
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
            </form>
    
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
    <!-- <script src="https://cdn.jsdelivr.net/npm/jquery@3.5.1/dist/jquery.slim.min.js" integrity="sha384-DfXdz2htPH0lsSSs5nCTpuj/zy4C+OGpamoFVy38MVBnE+IbbVYUew+OrCXaRkfj" crossorigin="anonymous"></script> -->
    <!-- <script>window.jQuery || document.write('<script src="../../node_modules/jquery/dist/jquery.min.js"><\/script>')</script><script src="../assets/js/bootstrap.bundle.min.js"></script> -->

    
    