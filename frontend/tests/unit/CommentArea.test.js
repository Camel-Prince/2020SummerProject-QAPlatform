import { mount } from '@vue/test-utils'
import CommentArea from '../../src/components/CommentArea.vue'

describe('测试评论组件', ()=> {
  const wapper = mount(CommentArea);
  it('测试data', ()=> {
    wapper.setData({textarea: 'sss'});
    expect(wapper.vm.textarea).toEqual('sss');
  })
})