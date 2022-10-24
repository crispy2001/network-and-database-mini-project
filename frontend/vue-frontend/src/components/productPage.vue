<template>
<body>
    <headerComponent></headerComponent>
    <main>

        <div class="container text-center mt-5">
            <div class=" text-center " style = "background-color: red; ">
                <img class="my-auto" src="@/assets/img/smile.png" alt="" style="width: auto; height: auto; max-width: 100%; max-height: 100%;">
            </div>
            <div class="col p-5" >
                <section class=" text-center">
                    <div class="container">
                        <h1 class = "p-3">PRODUCT NAME</h1>
                    </div>
                </section>
                <div class = "row">
                    <h4 class = "col">價錢：</h4>
                    <h4 class = "col">$$$</h4>
                </div>
                <div class = "row">
                    <h4 class = "col">商品數量：</h4>
                    <h4 class = "col">哈哈哈</h4>
                </div>
                <div class = "row">
                    <h4 class = "col">賣家：</h4>
                    <h4 class = "col">哈哈哈</h4>
                </div>
                <div class = "row">
                    <h4 class = "col">商品介紹：</h4>
                    <h4 class = "col">哈哈哈</h4>
                </div>
                <div class="row ">
                    <div class="col align-self-center">
                        <button class="btn btn-lg btn-dark btn-block" type="submit">add to chart</button>
                    </div>
                </div>
            </div>
        </div>
        <!-- <div class="container">
            <div class="row m-4" style = "min-height: 400px;">
                <div class="col-md-6 col-sm-12 text-center " style = "background-color: red; ">
                    <img class="my-auto" src="@/assets/img/smile.png" alt="" style="width: auto; height: auto; max-width: 100%; max-height: 100%;">
                </div>
                <div class="col p-5" >
                    <div class = "row">
                        <h4 class = "col">商品名稱：</h4>
                        <h4 class = "col">哈哈哈</h4>
                    </div>
                    <div class = "row">
                        <h4 class = "col">商品數量：</h4>
                        <h4 class = "col">哈哈哈</h4>
                    </div>
                    <div class = "row">
                        <h4 class = "col">商品名稱：</h4>
                        <h4 class = "col">哈哈哈</h4>
                    </div>
                    <div class = "row">
                        <h4 class = "col">商品名稱：</h4>
                        <h4 class = "col">哈哈哈</h4>
                    </div>
                    <div class = "row">
                        <h4 class = "col">去買單  </h4>
                    </div>
                </div>
            </div>
        </div> -->
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