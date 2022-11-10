
let $ = jQuery;
let $rows = $('.sku-value-tr');
let dic = {
  // FORMAT:
  // 'taobao-key' -> '1688 value'
};

$rows.each(function(index, elem){
  let phone = $(this).find('td[data-sku-key=适用手机型号]')[0].innerHTML
  let color = $(this).find('td[data-sku-key=颜色分类]')[0].innerHTML

  let srcArr = $(this).find('.next-select, .small, .select')
  let span_color = $(srcArr[0])
  let span_phone = $(srcArr[1])
  let val_id = $(span_color).attr('data-spm-anchor-id')


  let str = phone + '`' + color + ' ` ' + sel
  console.log("id = " + index + ' str=' + str)
});

